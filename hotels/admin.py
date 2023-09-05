from django.contrib import admin
from .models import *
# Register your models here.
# Iterate over all models in your app and register them
for model in [Hotel, Room, TimeSlot, Booking,HotelImages]:
    admin.site.register(model)

 
 # Get all models in the app
# app_models = apps.get_models()

# # Register each model in the admin panel
# for model in app_models:
#     admin.site.register(model)