import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Event


class EventConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("connected")
        await self.send({
            "type":"websocket.accept"
        })


        e = await self.events() 

        print(e)
        
        await self.send({
            "type":"websocket.send",
            "text": "Hello world"
        })
    
    async def websocket_receive(self,event):
        # print("receive", event)
        pass

    async def websocket_disconnect(self,event):
        pass

    @database_sync_to_async
    def events(self):
        return Event.objects.all()