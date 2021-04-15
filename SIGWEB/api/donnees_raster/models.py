from django.db import models

from api.donnees.models import Donnees
from api.user.models import User


class DonneesRaster(Donnees):
    area = models.IntegerField()
    perimeter = models.IntegerField()
    xCentroid = models.IntegerField()
    yCentroid = models.IntegerField()
    majorAxis = models.IntegerField()
    minAxis = models.IntegerField()
    orientation = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=True)


    class Meta(Donnees.Meta):
        pass


