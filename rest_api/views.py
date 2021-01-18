from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from .models import Gasstations, Pricedata
from .serializers import GasStationSerializer, PricedataSerializer

# Create your views here.

class GasStationViewSet(viewsets.ViewSet):

	def list(self, request):
		stations = Gasstations.objects.all()
		serializer = GasStationSerializer(stations, many=True)
		return Response(serializer.data)

class AllPrices(viewsets.ViewSet):

	def list(self, request, format=None):
		data = Pricedata.objects.all()
		serializer = PricedataSerializer(data, many=True)
		return Response(serializer.data)
	
	def post(self, request):
		raise Http404

class StationPrices(viewsets.ViewSet):

	def get_object(self, pk):
		try:
			return Pricedata.objects.filter(gasstationid=pk)
		except Pricedata.DoesNotExist:
			raise Http404

	def retrieve(self, request, pk, format=None):
		data = self.get_object(pk)
		serializer = PricedataSerializer(data, many=True)
		return Response(serializer.data)

	# def put(self, request, pk, format=None):
	# 	data = self.get_object(pk)
	# 	serializer = PricedataSerializer(data, data=request.data)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# def delete(self, request, pk, format=None):
	# 	data = self.get_object(pk)
	# 	data.delete()
	# 	return Response(status=status.HTTP_204_NO_CONTENT)