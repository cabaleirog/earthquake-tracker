from django.conf.urls import url
from locations import views


urlpatterns = [
    url(
        r'^locations$',
        views.get_all_locations,
        name='list_endpoint'
    ),
    url(
        r'^locations/add$',
        views.add_location,
        name='add_endpoint'
    ),
]
