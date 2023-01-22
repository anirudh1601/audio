from django.urls import path
from . import consumers
from . import views

websocket_urlpatterns = [
    path('stream/<room_stream_name>/room', consumers.ChatConsumer.as_asgi(),name='connection'),
    path('stream/<room_stream_name>', consumers.RoomConsumer.as_asgi(),name='room'),
]