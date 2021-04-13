from rest_framework import serializers
from django.db import models
from .models import Point


class PointSerializer(serializers.Serializer):
    nom = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    x = serializers.IntegerField()
    y = serializers.IntegerField()

    objects = models.Manager()

    def create(self, validated_data):
        return Point.objects.create(**validated_data)


