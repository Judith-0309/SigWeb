from rest_framework import serializers
from .models import Ligne
from django.db import models
from django.contrib.gis.db import models as gis_models





class LigneSerializer(serializers.Serializer):
    location = gis_models.PointField(srid=4326,blank=True, null=True)
    nom = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    longueur = serializers.IntegerField()
    taille = serializers.IntegerField()

    objects = models.Manager()

    def create(self, validated_data):
        return Ligne.objects.create(**validated_data)

