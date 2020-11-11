from datetime import datetime
from django.shortcuts import render
from . import models

# from django.http import HttpResponse


def all_rooms(request):
    all_rooms = models.Room.objects.all()

    return render(request, "all_rooms.html", context={"room": all_rooms})
