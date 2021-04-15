from django.db import models
from api.donnees.models import Donnees
from api.user.models import User


class Point(Donnees):
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    pass

    class Meta(Donnees.Meta):
        db_table = 'points'

