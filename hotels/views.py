from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
# hotels/views.py
from django.shortcuts import render
from .models import Room

def room_list_with_images_and_bookings(request):
    rooms = Room.objects.get_rooms_with_data()
    
    return render(request, 'hotels/room_list_and_bookings.html', {'rooms': rooms})

@api_view(['GET'])
def get_hotel_details(request):
    rooms = Room.objects.get_rooms_with_data().values()
    return JsonResponse({"rooms": list(rooms)})