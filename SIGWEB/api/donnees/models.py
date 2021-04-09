from django.db import models
from api.user.models import User


class Donnees(models.Model):
    type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=True)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.type

    class Meta:
        ordering = ['type']

