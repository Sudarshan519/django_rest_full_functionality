from django.db import models

from users.models import CustomUser
from django.db.models import Count, F
from django.db.models.functions import Concat
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class RoomManager(models.Manager):
    def get_rooms_with_data(self):
        return self.annotate(
            full_name=Concat(F('hotel__name'), models.Value(' - Room '), F('room_number')),
            image_url=F('image'),
            # total_bookings=Count('hotels_timeslot'),
            # bookings=Count('hotels_booking')
        )
        # .prefetch_related(
        #     # 'hotels_timeslot',
        #     'hotels_booking__user',
        #     'hotels_booking__room'
        # )
    
class HotelImages(models.Model):
    hotel = models.ForeignKey("hotels.Hotel", on_delete=models.CASCADE)
    image=image=models.ImageField(_("Hotel Images"), upload_to='media/hotels', height_field=None, width_field=None, max_length=None,null=False,blank=False)
# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    description = models.TextField()
    image=models.ImageField(_("Hotel Image"), upload_to='media/hotels', height_field=None, width_field=None, max_length=None,null=False,blank=False)
    def __str__(self):
        return self.name
    def image_URL(self):
        return self.image.url
    

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    bed_count = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(_("Room Image"), upload_to='media/hotels', height_field=None, width_field=None, max_length=None,null=False,blank=False)
    objects = RoomManager()
    def __str__(self):
        return f"Room {self.room_number} at {self.hotel}"
    


class TimeSlot(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Assuming you have a User model

    def __str__(self):
        return f"Booking for {self.room} by {self.user}"
    

