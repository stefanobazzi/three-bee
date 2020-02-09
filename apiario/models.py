from django.db import models
from arnia.models import Arnia


class Apiario(models.Model):
    nome = models.CharField(max_length=100)
    arnie = models.ManyToManyField(Arnia, related_name='apiari')

    def __str__(self):
        return self.nome