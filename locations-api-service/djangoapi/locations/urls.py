from django.conf.urls import url
from locations import views


urlpatterns = [
    url(
        r'^$',
        views.get_all_locations,
        name='list_endpoint'
    ),
    url(
        r'^add$',
        views.add_location,
        name='add_endpoint'
    ),
]
