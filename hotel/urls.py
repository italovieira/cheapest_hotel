from django.urls import path

from hotel.views import CheapestHotelView


app_name = 'hotel'

urlpatterns = [
    path('', CheapestHotelView.as_view(), name='cheapest'),
]
