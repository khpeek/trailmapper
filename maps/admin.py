from django.contrib.gis import admin
from .models import Map

admin.site.register(Map, admin.OSMGeoAdmin)
