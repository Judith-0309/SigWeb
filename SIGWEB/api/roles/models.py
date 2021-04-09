from django.db import models
# Create your models here.


CHOICES = [
    ('ADMIN','Admin.'),
    ('USER','User'),
]
class Role(models.Model):
    roles = models.CharField(max_length=100,choices=CHOICES)
    objects = models.Manager()

    def __str__(self):
        return "%s" % self.roles