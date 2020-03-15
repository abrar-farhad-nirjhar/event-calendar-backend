from django.db import models

# Create your models here.

class Event(models.Model):
    username = models.CharField(max_length=255, blank=False, null=False, default="default")
    event_name = models.CharField(max_length=400, blank=False, null=False)
    event_description = models.TextField(blank=False, null=False)
    day = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.event_name