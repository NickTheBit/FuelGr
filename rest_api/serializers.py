from rest_framework import serializers

from .models import Gasstations, Pricedata, Orders

class GasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasstations
        fields = '__all__'

class PricedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricedata
        fields = '__all__' 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'