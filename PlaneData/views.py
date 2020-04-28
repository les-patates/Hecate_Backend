from django.shortcuts import render
from .serializers import WaypointSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Waypoint


# Create your views here.
class UpdateWaypoint(APIView):

    def get(self, request, format=None):
        waypoints = Waypoint.objects.all()
        serializer = WaypointSerializer(waypoints,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = WaypointSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = Waypoint.objects.all()
            ret = WaypointSerializer(response,many=True)
            return Response(ret.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteWaypoint(APIView):
    def delete(self,request,pk,format=None):
        try:
            element = Waypoint.objects.get(pk=pk)
        except:
            return Response(None,status=status.HTTP_400_BAD_REQUEST)
        element.delete()
        waypoints = Waypoint.objects.all()
        serializer = WaypointSerializer(waypoints,many=True)
        return Response(serializer.data)
