from rest_framework import serializers
# from .models import User


class CompteSerializer(serializers.Serializer):
        datecreation = serializers.DateTimeField()
        numerocompte = serializers.IntegerField()
