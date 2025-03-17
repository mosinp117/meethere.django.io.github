from django.shortcuts import render
import random
import string

def generate_meeting_code():
    """Generate a random meeting room name"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def meeting_room(request, room_name=None):
    """Render the meeting room"""
    if not room_name:
        room_name = generate_meeting_code()  # Generate random room name if not provided
    return render(request, "meetings/meeting.html", {"room_name": room_name})
