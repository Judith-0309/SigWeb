from rest_framework import serializers
from .models import Ligne
from django.db import models



class LigneSerializer(serializers.Serializer):
    nom = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    longueur = serializers.IntegerField()
    taille = serializers.IntegerField()

    objects = models.Manager()

    def create(self, validated_data):
        return Ligne.objects.create(**validated_data)

