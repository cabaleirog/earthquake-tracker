from rest_framework.response import Response
from rest_framework.decorators import api_view

from locations.models import Location
from locations.serializers import LocationSerializer


@api_view(['GET'])
def get_all_locations(request):
    """Return all locations stored in the database."""
    locations = Location.objects.all()
    return Response({
        'message': f'{len(locations)} locations found.',
        'data': LocationSerializer(locations, many=True).data
    })


@api_view(['POST'])
def add_location(request):
    """Create a new database record for the provided location."""
    identifier = request.data.get('identifier')
    name = request.data.get('name')
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')

    if Location.objects.filter(identifier=identifier):
        return Response({
            'message': f'Location already exists for indentifier {identifier}',
            'data': []
        })

    location = Location.objects.create(
        identifier=identifier,
        name=name,
        latitude=latitude,
        longitude=longitude,
    )

    return Response({
        'message': 'Location added successfully',
        'data': LocationSerializer(location).data
    })
