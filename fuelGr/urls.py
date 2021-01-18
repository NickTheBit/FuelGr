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
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'station', views.GasStationViewSet, basename="")
router.register(r'station/<int:pk>', views.GasStationViewSet , basename="station")
router.register(r'price', views.StationPrices, basename="")
router.register(r'price/<int:pk>', views.StationPrices , basename="price")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
	path('admin/', admin.site.urls),
	path('rest/', include('rest_framework.urls', namespace='rest_framework')),
	path('api/', include(router.urls))
	# path("price/",views.AllPrices.as_view()),
	# path("price/<int:pk>", views.StationPrices.as_view()),
]
