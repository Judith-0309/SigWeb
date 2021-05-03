from rest_framework import serializers
from .models import DonneesRaster
from django.db import models
from django.contrib.gis.db import models as gis_models





class DonneesRasterSerializer(serializers.Serializer):
    area = serializers.IntegerField()
    perimeter = serializers.IntegerField()
    xCentroid = serializers.IntegerField()
    yCentroid = serializers.IntegerField()
    majorAxis = serializers.IntegerField()
    minAxis = serializers.IntegerField()
    orientation = serializers.IntegerField()
    location = gis_models.PointField(srid=4326,blank=True, null=True)


    objects = models.Manager()

    def create(self, validated_data):
        return DonneesRaster.objects.create(**validated_data)

