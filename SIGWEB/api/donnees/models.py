from django.db import models
from api.user.models import User


class Donnees(models.Model):
    type = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=True, related_name="%(app_label)s_%(class)s_related", related_query_name="%(app_label)s_%(class)ss",)
    objects = models.Manager()

    # def __str__(self):
    #     return "%s" % self.type

    class Meta:
        abstract = True
        ordering = ['type']




