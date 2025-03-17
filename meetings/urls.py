from django.urls import path
from .views import meeting_room

urlpatterns = [
    path('meet/<str:room_name>/', meeting_room, name='meeting_room'),
    path('meet/', meeting_room, name='new_meeting'),  # New meeting without name
]
