from django.db import models

from task.models import Task


class Arnia(models.Model):
    nome = models.CharField(max_length=100)
    task = models.ManyToManyField(Task)

    def __str__(self):
        return self.nome

    def get_temp(self):
        """La temperatura è acquisita da un sensore e viene letta da un API -> GetTemp(IdArnia)."""
        pass