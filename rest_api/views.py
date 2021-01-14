from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions

from .models import Gasstations
from .serializers import GasStationSerializer

# Create your views here.

class GasStationViewSet(viewsets.ModelViewSet):
	queryset = Gasstations.objects.all()
	serializer_class = GasStationSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
