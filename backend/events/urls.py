
from django.urls import path, include
from .views import EventViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('events', EventViewset)
urlpatterns = [
    
]+router.urls

