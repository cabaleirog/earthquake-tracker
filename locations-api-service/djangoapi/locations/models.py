from django.db import models


class Location(models.Model):
    identifier = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
