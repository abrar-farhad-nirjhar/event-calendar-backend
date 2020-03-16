import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Event
from .serializers import EventSerializer
import datetime
from asgiref.sync import async_to_sync
import channels.layers
# import channels
from django.db.models.signals import post_save
from django.dispatch import receiver



class EventConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connected")
        print(self.channel_layer)
        await self.send({
            "type":"websocket.accept"
        })

        await self.send_data()
        
    
    
    async def send_data(self):
        events = await self.events()

        serializer = EventSerializer(events, many=True)
        await self.send({
                "type":"websocket.send",
                "text": json.dumps(serializer.data)
                

            })

    
    async def websocket_receive(self,event):
        if event is not None:
            print("receive", event)
            await self.send_data()
        

    async def websocket_disconnect(self,event):
        pass

    @database_sync_to_async
    def events(self):
        today = datetime.datetime.today()
        return Event.objects.filter(day__gte=today)

    
    @staticmethod   
    @receiver(post_save, sender=Event)
    def scooter_post_update(sender, instance, created, **kwargs):
        
        channel_layer = channels.layers.get_channel_layer()
        print("hakuna")
        print(channel_layer)
        # channel_layer.send('event',{
        #     "type":"websocket.send",
        #     "data": "hakuna matata"
        # })
        async_to_sync(channel_layer.send)("message",{
            "text":"hakuna"
        })
        
