"""fuelGr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_api.views import GasStationViewSet

# # Serializers define the API representation.
# class GasStationSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Gasstations
# 		fields = ['gasstationid', 'fuelcompid', 'gasstationlat', 'gasstationlong']

# # ViewSets define the view behavior.
# class GasStationViewSet(viewsets.ModelViewSet):
# 	queryset = Gasstations.objects.all()
# 	serializer_class = GasStationSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'station', GasStationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include(router.urls)),
	path('rest/', include('rest_framework.urls', namespace='rest_framework'))
]
