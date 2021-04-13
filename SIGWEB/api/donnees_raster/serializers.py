from rest_framework import serializers
from .models import DonneesRaster
from django.db import models



class DonneesRasterSerializer(serializers.Serializer):
    area = serializers.IntegerField()
    perimeter = serializers.IntegerField()
    xCentroid = serializers.IntegerField()
    yCentroid = serializers.IntegerField()
    majorAxis = serializers.IntegerField()
    minAxis = serializers.IntegerField()
    orientation = serializers.IntegerField()


    objects = models.Manager()

    def create(self, validated_data):
        return DonneesRaster.objects.create(**validated_data)

