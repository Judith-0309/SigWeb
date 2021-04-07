from django.db import models

# Create your models here.


class User(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    motdepass = models.CharField(max_length=100,default=True)
