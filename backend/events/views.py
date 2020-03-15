from django.shortcuts import render
import datetime
from .models import Event
from rest_framework import viewsets
from rest_framework import generics
from .serializers import EventSerializer
# Create your views here.
# d = datetime.datetime.strptime(ds, '%Y-%m-%d')

class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    # def create(self,request):
    #     print(request)






