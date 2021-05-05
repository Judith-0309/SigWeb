from rest_framework import serializers
from django.db import models
from .models import Point
from django.contrib.gis.db import models as gis_models





class PointSerializer(serializers.Serializer):
    location = gis_models.PointField(srid=4326,blank=True, null=True)
    nom = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    x = serializers.IntegerField()
    y = serializers.IntegerField()

    objects = models.Manager()

    def create(self, validated_data):
        return Point.objects.create(**validated_data)


