from django.db import models
from api.donnees.models import Donnees
from api.user.models import User


class Polygone(Donnees):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    superficie = models.IntegerField()
    taille = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    pass

    class Meta(Donnees.Meta):
        db_table = 'polygones'

