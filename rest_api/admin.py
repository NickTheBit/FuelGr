from django.contrib import admin
from .models import Gasstations ,Orders, Pricedata

# Register your models here.

admin.site.register(Gasstations)
admin.site.register(Orders)
admin.site.register(Pricedata)