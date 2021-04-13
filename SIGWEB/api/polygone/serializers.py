from rest_framework import serializers
from django.db import models
from .models import Polygone


class PolygoneSerializer(serializers.Serializer):
    nom = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    superficie = serializers.IntegerField()
    taille = serializers.IntegerField()

    objects = models.Manager()

    def create(self, validated_data):
        return Polygone.objects.create(**validated_data)