from datetime import datetime, timedelta
from functools import cache

from rest_framework.response import Response
from rest_framework.decorators import api_view

from locations.models import Location
from earthquakes.models import Earthquake
from earthquakes.serializers import EarthquakeSerializer

from earthquakes.utils import get_logger, pull_usgs_data, check_missing_dates, create_capture_ranges, distance


logger = get_logger(__name__)


@api_view(['GET'])
def get_closest_earthquake(request):
    """..."""
    location_identifier = request.GET.get('location')
    starttime = datetime.strptime(request.GET.get('starttime'), '%Y-%m-%d')
    endtime = datetime.strptime(request.GET.get('endtime'), '%Y-%m-%d')

    location = Location.objects.get(identifier=location_identifier)
    logger.debug(location)

    # TODO: Check if the result is on cache, and return if found

    closest = _get_closest_earthquake(
        location.latitude, location.longitude, starttime, endtime)

    if closest:
        return Response({
            'message': 'Earthquake found.',
            'data': EarthquakeSerializer(closest, many=False).data
        })

    return Response({
        'message': 'Earthquake not found for the given contrains.',
        'data': None
    })


@cache
def _get_closest_earthquake(latitude, longitude, start_time, end_time):
    if isinstance(start_time, str):
        start_time = datetime.strptime(start_time, '%Y-%m-%d')
    if isinstance(end_time, str):
        end_time = datetime.strptime(end_time, '%Y-%m-%d')

    missing_dates = check_missing_dates(start_time, end_time)

    date_ranges_to_capture = create_capture_ranges(missing_dates)
    logger.debug(date_ranges_to_capture)

    # Fetch missing data
    for (drs, dre) in date_ranges_to_capture:
        logger.debug('%s %s', drs, dre)
        earthquakes_data = pull_usgs_data(drs, dre)
        for data in earthquakes_data:
            Earthquake.from_usgs_json_data(data)

    # As end_time is provided at the start of the day, we will force it to
    # the end of the day by adding a day to it.
    end_time_midnight = end_time + timedelta(days=1)

    # Calculate the closest
    distance_array = []
    earthquakes = Earthquake.objects.filter(
        time__range=[start_time, end_time_midnight])
    for earthquake in earthquakes:
        d = distance(
            latitude, earthquake.latitude, longitude, earthquake.longitude)
        distance_array.append((d, earthquake))
        logger.debug('%.0f -> %s | %s %s', d, earthquake, earthquake.latitude, earthquake.longitude)

    if not distance_array:
        # There were no earthquakes meeting the contrains for the period.
        return None

    distance_array.sort(key=lambda x: x[0])
    logger.debug(distance_array[0])

    return distance_array[0][1]
