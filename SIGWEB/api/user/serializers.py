from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    nom = serializers.CharField(max_length=100)
    prenom = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    motdepass = serializers.CharField(max_length=100,default=True)

    class Meta:
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create(**validated_data)

