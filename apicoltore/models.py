from django.contrib.auth.models import User
from django.db import models

from apiario.models import Apiario


class Apicoltore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apiari = models.ManyToManyField(Apiario, related_name='apicoltori')

    def __str__(self):
        return self.user.username