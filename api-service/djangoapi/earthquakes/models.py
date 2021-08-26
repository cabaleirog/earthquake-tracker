import pytz
from datetime import datetime

from django.db import models, IntegrityError


class Earthquake(models.Model):
    event_id = models.CharField(max_length=255, unique=True)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    magnitude = models.FloatField(null=False)
    place = models.TextField(null=True)
    time = models.DateTimeField(null=False)
    magnitude_type = models.CharField(max_length=5)
    title = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    @classmethod
    def from_usgs_json_data(cls, data):
        # Check if it already exists
        earthquake = cls.objects.filter(event_id=data.get('id')).first()
        if earthquake:
            return earthquake

        # Create new record in the database
        earthquake = cls(
            event_id=data.get('id'),
            latitude=data.get('geometry').get('coordinates')[1],
            longitude=data.get('geometry').get('coordinates')[0],
            magnitude=data.get('properties').get('mag'),
            place=data.get('properties').get('place'),
            time=datetime.fromtimestamp(
                data.get('properties').get('time') // 1000, pytz.utc),
            magnitude_type=data.get('properties').get('magType'),
            title=data.get('properties').get('title'),
        )
        try:
            earthquake.save()
        except IntegrityError:
            # FIXME: The record seems to have been saved while creating this.
            earthquake = cls.objects.filter(event_id=data.get('id')).first()
        return earthquake

    def __str__(self):
        return self.title
