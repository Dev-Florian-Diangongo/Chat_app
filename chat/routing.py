from django.urls import path
from .consumers import *
websocket_urlpatterns = [
    path("ws/chatroom/<chatroom_name>",ChatRoomConsumers.as_asgi()) # chatroomname is the group that i'll get in consumers
]