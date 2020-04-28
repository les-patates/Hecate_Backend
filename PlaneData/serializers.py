from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Waypoint

class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ['lat','lon']
        
