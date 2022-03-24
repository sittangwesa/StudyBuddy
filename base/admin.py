from http.client import NETWORK_AUTHENTICATION_REQUIRED
from django.contrib import admin

# Register your models here.

from .models import Room, Topic
from .models import Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

