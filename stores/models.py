from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.validators import MaxValueValidator, MinValueValidator

class StoreType(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(unique=True, max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["created_at"]

# Create your models here.
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    rating = models.FloatField(null=True, blank=True)
    store_type = models.CharField(max_length=50, null=True, blank=True)
    opening_hour = models.TimeField(null=True, blank=True)
    closing_hour = models.TimeField(null=True, blank=True)
    city = models.CharField(max_length=50)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location = models.PointField(null=True, blank=True, srid=4326)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)