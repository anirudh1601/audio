from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer,JsonWebsocketConsumer
from channels.consumer import AsyncConsumer
import json
from asgiref.sync import async_to_sync
import base64
import subprocess
import threading
from .decorators import start_new_thread
import numpy as np
#ffmpeg_proc = subprocess.Popen('ffmpeg -y -f webm -i - -ac 1 -ar 16000  -f wav /tmp/out.wav', shell=True, stdin=subprocess.PIPE)
# from supyr_struct import *
import struct
import array
from django.contrib.auth.models import User



class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.room_name = self.scope['url_route']['kwargs']['room_stream_name']
        self.room_group_name = 'stream_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
        # print(self.channel_name)

        

        print('connected')
    def disconnect(self,close_code):
        self.disconnect()

    def receive(self,text_data=None, bytes_data=None):
        #print(event)
        my_string =bytes_data
        # print(my_string)
        sent = self.scope["user"].username
        # ng
        sent_by = str.encode(sent)
        # print(sent_by)
        # print(my_string)
        # if '123' in my_string:
        #     name = my_string.replace('123','')
            
        #     a = name.encode('utf-8')
            
        # audio = a

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'text':my_string,
                'sent_by':sent            }
        )
    # @start_new_thread
    # def receive(self,bytes_data=None,text_data=None):
    #     #print(event)
    #     my_string = bytes_data
    #     my_string =json.loads(text_data)
    #     name = my_string['message']
    #     audio = my_string['audio']
    #     # print(my_string)
    #     # print(my_string)
    #     #print(text_data)
    #     #print(len(my_string))
    #     #print(my_string)
    #     async_to_sync(self.channel_layer.group_send)(
    #         self.room_group_name,
    #         {
    #             'type':'chat_message',
    #             'text':my_string,
    #             'audio':audio
    #         },
            
    #     ) 

    
    # @start_new_thread
    def chat_message(self,event):
        #print('chat_message',event)
        message = event['text']
        sent_by = event['sent_by']
        # audio = event['audio']
        #print(message)
        # self.send(bytes_data=(message))
        self.send(text_data=(
            sent_by
            # 'audio':audio
        )) 
        self.send(bytes_data=(
            message
            # 'audio':audio
        )) 
        
    
    

  


# def to_bytes(s):
#     if type(s) is bytes:
#         return s
#     elif type(s) is str or (sys.version_info[0] < 3 and type(s) is unicode):
#         return codecs.encode(s, 'utf-8')
#     else:
#         raise TypeError("Expected bytes or string, but got %s." % type(s))       


abc = []
class RoomConsumer(WebsocketConsumer):
    def connect(self):
        name = self.scope["user"]
        
        user = User.objects.get(username=name).username
        if user not in abc:
            abc.append(user)
        self.room_name = self.room_name = self.scope['url_route']['kwargs']['room_stream_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message1',
                'name':abc,
              
            }
        )
        

        

        print('connected')
    def disconnect(self,close_code):
        self.disconnect()

    def receive(self,text_data=None, bytes_data=None):
        #print(event)
        my_string =json.loads(text_data)
        print(my_string)
        name = my_string['name']
        data =  my_string['data']
        if isinstance(data,int):
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':'chat_message',
                    'name':name,
                    'data':data,
                }
            )
        else:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type':'chat_message1',
                    'name':name,
                    'data':data,
                }
            )

    def chat_message(self,event):
        #print('chat_message',event)
        name = event['name']
        data = event['data']
        # audio = event['audio']
        #print(message)
        # self.send(bytes_data=(message))
        self.send(text_data=json.dumps({
            'name':name,
            'data':data
            # 'audio':audio
        })) 

    
    def chat_message1(self,event):
        #print('chat_message',event)
        name = event['name']
        # audio = event['audio']
        #print(message)
        # self.send(bytes_data=(message))
        self.send(text_data=json.dumps({
            'name':name,
            # 'id':name.id,
            'data':'connected'
        #  'data':data
            # 'audio':audio
        }))
    
    

  


   
        
        
