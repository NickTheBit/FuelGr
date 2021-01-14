from rest_framework import serializers

from .models import Gasstations

class GasStationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gasstations
        fields = ["fuelcompnormalname","fuelcompid","gasstationlat","gasstationlong"]

