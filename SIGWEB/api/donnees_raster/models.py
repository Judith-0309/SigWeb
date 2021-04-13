from django.db import models

from api.donnees.models import Donnees


class DonneesRaster(Donnees):
    area = models.IntegerField()
    perimeter = models.IntegerField()
    xCentroid = models.IntegerField()
    yCentroid = models.IntegerField()
    majorAxis = models.IntegerField()
    minAxis = models.IntegerField()
    orientation = models.IntegerField()


    class Meta(Donnees.Meta):
        pass


