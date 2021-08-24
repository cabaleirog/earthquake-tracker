from rest_framework import serializers
from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'pk', 'identifier', 'name', 'latitude', 'longitude', 'created'
        )
        read_only_fields = ('created_date',)
