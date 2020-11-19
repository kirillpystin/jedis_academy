"""Модуль, отвечающий за создание класса `Planet`"""
from django.db import models

from .planet import Planet


class Jedi(models.Model):
    """Класс, содержащий информацию о джедае.

    Attributes:
        name(CharField): Имя.
        planet(Planet): Планета.

    """

    name = models.CharField(max_length=200, verbose_name="Имя")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name="Планета")

    class Meta:
        verbose_name = "Джедай"
        verbose_name_plural = "Джедаи"

    def __str__(self):
        return self.name

    __slots__ = ("name", "planet")
