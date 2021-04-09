from django.db import models

# Create your models here.


class Compte(models.Model):
        datecreation = models.DateTimeField()
        numerocompte = models.IntegerField()
        objects = models.Manager()

def __str__(self):
        return "%s the place" % self.nom
