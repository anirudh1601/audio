from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('stream/<room_stream_name>', views.audio,name="audio"),

]
