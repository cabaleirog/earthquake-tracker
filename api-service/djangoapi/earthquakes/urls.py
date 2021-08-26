from django.conf.urls import url
from earthquakes import views


urlpatterns = [
    url(
        r'^$',
        views.get_closest_earthquake,
        name='closest_earthquake'
    ),
]
