from django.shortcuts import render
from .models import Stream
from django.views.decorators.csrf import csrf_exempt

# import eventlet
# async_mode = eventlet
# import os
# from django.http import HttpResponse
# import socketio

# basedir = os.path.dirname(os.path.realpath(__file__))
# io = socketio.Server(async_mode='eventlet')

# @io.on('connection-bind')
# def connection_bind(request):
#     print("connected")
#     return HttpResponse('hello')

# @io.on('message')
# def message(data):
#     print(data)
#     sio.emit('test',data)
# @io.on('disconnect')
# def test_disconnect(sid):
#     print("Disconnected")


# Create your views here.
@csrf_exempt
def audio(request,room_stream_name):
    # print(request.body)
    user = Stream.objects.get(slug=room_stream_name)
    print(user)
    return render(request,'multiaudio/a.html',{'name':request.user.username})


