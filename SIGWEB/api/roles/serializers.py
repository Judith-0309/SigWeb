from rest_framework import serializers
from .models import Role, CHOICES



class RoleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    roles = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Role.objects.create(**validated_data)