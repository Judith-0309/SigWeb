from __future__ import unicode_literals
from django.contrib.gis.db import models as gis_models
from api.donnees.models import Donnees
from api.user.models import User
from django.db import models



class Point(Donnees):
    location = gis_models.PointField(srid=4326, blank=True, null=True)
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    pass

    class Meta(Donnees.Meta):
        db_table = 'point'

