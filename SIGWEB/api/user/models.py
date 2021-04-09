from django.db import models
from ..compte.models import Compte
from ..roles.models import Role


class User(models.Model):
    compte = models.OneToOneField(
        "Compte",
        on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    motdepass = models.CharField(max_length=100,default=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,default=True)
    objects = models.Manager()


    def __str__(self):
        return "%s the user" % self.nom

    class Meta:
        ordering = ['nom']
