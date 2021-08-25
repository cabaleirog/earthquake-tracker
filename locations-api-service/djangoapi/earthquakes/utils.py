import logging
import json
from functools import cache
from datetime import timedelta
from math import radians, cos, sin, asin, sqrt

import requests


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


def build_query_url(start_date, end_date, min_magnitude):
    """

    Args:
        start_date (datetime):
        end_date (datetime):
        min_magnitude (float):

    Returns:
        str: The url with the relevant query parameters.

    """
    return (f'https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?'
            f'starttime={start_date.strftime("%Y-%m-%d")}&'
            f'endtime={end_date.strftime("%Y-%m-%d")}&'
            f'minmagnitude={min_magnitude}&orderby=time')


def pull_usgs_data(start_date, end_date, min_magnitude=5.0):
    url = build_query_url(start_date, end_date, min_magnitude)
    response = requests.get(url)
    data = json.loads(response.text)
    return data.get('features')


@cache
def check_missing_dates(start_date, end_date):
    """

    Args:
        start_date (datetime):
        end_date (datetime):



    Returns:
        List[datetime]

    """
    # TODO: Implement this, for now, everything is missing
    ans = []
    current_date = start_date
    while current_date <= end_date:
        ans.append(current_date)
        current_date = current_date + timedelta(days=1)
    return ans


def create_capture_ranges(dates, max_gap=30):
    """Return a list of time ranges.

       Each range represents the minimum possible range that covers everything
       within the `max_gap` number of days.

       Args:
           dates: (List[datetime])
           max_gap (int): Max number of days in any range
    """
    dates = sorted(dates)
    groups = []
    i = 0
    while i < len(dates):
        start = dates[i]
        for j in range(i, len(dates)):
            if (dates[j] - dates[i]) > timedelta(days=max_gap):
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
