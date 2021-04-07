from django.db import models

# Create your models here.


class Compte(models.Model):
        datecreation = models.DateTimeField()
        numerocompte = models.IntegerField()
        objects = models.Manager()
