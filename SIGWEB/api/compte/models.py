from django.db import models

# Create your models here.


class Compte(models.Model):
        datecreation = models.DateTimeField(auto_now_add=True)
        numerocompte = models.IntegerField()
