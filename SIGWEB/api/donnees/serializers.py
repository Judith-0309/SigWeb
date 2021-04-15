from rest_framework import serializers

from api.donnees.models import Donnees


class DonneesSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=100)

    def donnees_create(self, validated_data):
        return Donnees.objects.create(**validated_data)
