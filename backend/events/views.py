from django.shortcuts import render
import datetime
from .models import Event
from rest_framework import viewsets
from rest_framework import generics
from .serializers import EventSerializer


class EventViewset(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class UpcomingEventsList(generics.ListAPIView):
    serializer_class = EventSerializer
    

    def get_queryset(self):
        today = datetime.datetime.today()
        return Event.objects.filter(day__gte=today)






