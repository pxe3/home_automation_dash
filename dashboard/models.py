from django.db import models

# Create your models here.
class SmartLight(models.Model):
    name = models.CharField(max_length=100)
    is_on = models.BooleanField(default=False)
    brightness = models.PositiveIntegerField(default=0)
    room = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class SmartFan(models.Model):
    name = models.CharField(max_length=100)
    is_on = models.BooleanField(default=False)
    speed = models.PositiveIntegerField(default=0)
    rotating = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
