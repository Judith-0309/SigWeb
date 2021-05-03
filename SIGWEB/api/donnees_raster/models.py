from __future__ import unicode_literals
from django.db import models
from api.donnees.models import Donnees
from api.user.models import User
from django.contrib.gis.db import models as gis_models


class DonneesRaster(Donnees):
    area = models.IntegerField()
    perimeter = models.IntegerField()
    xCentroid = models.IntegerField()
    yCentroid = models.IntegerField()
    majorAxis = models.IntegerField()
    minAxis = models.IntegerField()
    orientation = models.IntegerField()
    location = gis_models.PointField(srid=4326,blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=True)


    class Meta(Donnees.Meta):
        pass


