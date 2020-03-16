
from django.urls import path, include
from .views import EventViewset, UpcomingEventsList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('events', EventViewset)
urlpatterns = [
    path('upcoming', UpcomingEventsList.as_view())
]+router.urls

