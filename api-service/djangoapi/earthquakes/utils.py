import logging
import json
from functools import cache
from datetime import timedelta
from math import radians, cos, sin, asin, sqrt

import requests

from earthquakes.models import Earthquake


def get_logger(name, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.hasHandlers():
        # create console handler
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # create formatter
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(name)s [%(filename)s:%(lineno)d] %(message)s')  # noqa E501

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

    return logger


logger = get_logger(__name__)


def build_query_url(start_date, end_date, min_magnitude):
    """Return a valid URL to pull earthquake data.

    https://earthquake.usgs.gov/fdsnws/event/1/#parameters

    All times use ISO8601 Date/Time format. Unless a timezone is specified,
    UTC is assumed. Examples:

    2021-08-26, Implicit UTC timezone, and time at start of the day (00:00:00)
    2021-08-26T00:20:44, Implicit UTC timezone.
    2021-08-26T00:20:44+00:00, Explicit timezone.

    Args:
        start_date (datetime): The start of the period.
        end_date (datetime): The end of the period.
        min_magnitude (float): The minimim magnitude to fetch.

    Returns:
        str: The url with the relevant query parameters.

    """
    query_end_date = end_date + timedelta(days=1)  # As time starts at 00:00:00
    return (f'https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?'
            f'starttime={start_date.strftime("%Y-%m-%d")}&'
            f'endtime={query_end_date.strftime("%Y-%m-%d")}&'
            f'minmagnitude={min_magnitude}&orderby=time')


def pull_usgs_data(start_date, end_date, min_magnitude=5.0):
    """Retrieve data from the USGS for a given period.

    Args:
        start_date (datetime): The start of the period.
        end_date (datetime): The end of the period.
        min_magnitude (Optional[float]): The minimim magnitude to fetch.

    Returns:
        List: All earthquakes for the period with minimum magnitude.

    """
    url = build_query_url(start_date, end_date, min_magnitude)
    logger.debug(url)
    response = requests.get(url)
    data = json.loads(response.text)
    return data.get('features')


@cache
def check_missing_dates(start_date, end_date):
    """Return the dates which are not currently stored in our database.

    Args:
        start_date (datetime): The initial date.
        end_date (datetime): The final date.

    Returns:
        List[datetime]: All missing dates for the period.

    """
    # TODO: This implementation could use some improvement.
    # A better implementation could include Redis instead of checking the DB.

    objs = Earthquake.objects.all().filter(time__range=(start_date, end_date +
                                                        timedelta(days=1)))
    seen = {x.time.date() for x in objs}
    all_dates = {
        (start_date + timedelta(days=i)).date()
        for i in range((end_date - start_date).days + 1)
    }
    return list(all_dates.difference(seen))


def create_capture_ranges(dates, max_gap=360):
    """Return a list of time ranges.

       Each range represents the minimum possible range that covers everything
       within the `max_gap` number of days.

       Args:
           dates: (List[datetime]): Dates to group.
           max_gap (int): Max number of days in any range.
    """
    dates = sorted(dates)
    groups = []
    i = 0
    while i < len(dates):
        start = dates[i]
        for j in range(i, len(dates)):
            if (dates[j] - dates[i]) >= timedelta(days=max_gap):
                i = j
                break
            end = dates[j]
        else:  # no-break
            groups.append((start, end))
            break
        groups.append((start, end))
        i = j
    return groups


# Cortesy of geek-for-geeks.
def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return (c * r)
