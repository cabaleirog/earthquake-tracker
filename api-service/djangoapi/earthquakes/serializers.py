from rest_framework import serializers
from earthquakes.models import Earthquake


class EarthquakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earthquake
        fields = ('event_id', 'latitude', 'longitude', 'magnitude', 'place',
                  'time', 'magnitude_type', 'title')
