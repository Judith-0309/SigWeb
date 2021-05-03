from rest_framework import serializers
from .models import Polygone
from django.db import models
from django.contrib.gis.db import models as gis_models


class PolygoneSerializer(serializers.Serializer):
    location = gis_models.PointField(srid=4326,blank=True, null=True)
    nom = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    superficie = serializers.IntegerField()
    taille = serializers.IntegerField()

    objects = models.Manager()

    def create(self, validated_data):
        return Polygone.objects.create(**validated_data)