from django.db import models
from api.donnees.models import Donnees


class Point(Donnees):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    pass

    class Meta(Donnees.Meta):
        db_table = 'points'

