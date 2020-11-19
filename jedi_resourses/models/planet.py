"""Модуль, отвечающий за создание класса `Planet`"""
from django.db import models


class Planet(models.Model):
    """Класс, содержащий информацию о планете.

    Attributes:
        name(TextField): Наименование планеты.

    """

    name = models.TextField(verbose_name="Планета")

    class Meta:
        verbose_name = "Планета"
        verbose_name_plural = "Планеты"

    def __str__(self):
        return self.name

    __slots__ = ("name",)
