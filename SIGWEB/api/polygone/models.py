from django.db import models
from api.donnees.models import Donnees


class Polygone(Donnees):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    superficie = models.IntegerField()
    taille = models.IntegerField()
    pass

    class Meta(Donnees.Meta):
        db_table = 'polygones'

