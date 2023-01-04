"""Models do core"""
from django.db import models


class Pessoa(models.Model):
    """Modelo de pessoa"""
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
