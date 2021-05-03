from rest_framework import serializers
from django.db import models
from .models import Points
from django.contrib.gis.db import models as gis_models







class PointsSerializer(serializers.Serializer):
    location = gis_models.PointField(srid=4326,blank=True, null=True)
    nom = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    x = serializers.IntegerField()
    y = serializers.IntegerField()

    objects = models.Manager()

    def create(self, validated_data):
        return Points.objects.create(**validated_data)


