from rest_framework import serializers
from .models import Compte


class CompteSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        datecreation = serializers.DateTimeField()
        numerocompte = serializers.IntegerField()

        class Meta:
                fields = '__all__'

        def create(self, validated_data):
                return Compte.objects.create(**validated_data)

