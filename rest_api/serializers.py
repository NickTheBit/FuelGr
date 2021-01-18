from rest_framework import serializers

from .models import Gasstations, Pricedata

class GasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasstations
        fields = '__all__'

class PricedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricedata
        fields = '__all__' 