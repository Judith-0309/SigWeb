from rest_framework import serializers
# from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nom = serializers.CharField(max_length=100)
    prenom = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    motdepass = serializers.CharField(max_length=100,default=True)


# class UserForm(forms.Form):
#     nom = forms.CharField(max_length=100)
#     prenom = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100)
#     motdepass = forms.CharField(max_length=100,default=True)

