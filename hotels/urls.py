 
# hotels/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('room-list/', views.room_list_with_images_and_bookings, name='room-list-with-images-and-bookings'),
    path('rooms',views.get_hotel_details)
]