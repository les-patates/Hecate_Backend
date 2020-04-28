from django.db import models

# Create your models here.
class PlaneData(models.Model):
    lat = models.FloatField()
    lon =  models.FloatField()
    battery = models.FloatField()


class Waypoint(models.Model):
    lat = models.FloatField()
    lon =  models.FloatField()
