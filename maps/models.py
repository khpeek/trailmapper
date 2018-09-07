from django.db import models
import django.contrib.gis.db.models


class Map(models.Model):
    image = models.ImageField()
    northeast = django.contrib.gis.db.models.PointField()
    southwest = django.contrib.gis.db.models.PointField()
