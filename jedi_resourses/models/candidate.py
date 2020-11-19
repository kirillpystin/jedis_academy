"""Модуль, отвечающий за создание класса `Candidate`"""
from django.db import models

from .planet import Planet


class Candidate(models.Model):
    """Класс, содержащий информацию о кандидате.

    Attributes:
        name(CharField): Имя.
        planet(Planet): Планета.
        old(IntegerField): Возраст.
        email(EmailField): Электронная почта.

    """

    name = models.CharField(max_length=200, verbose_name="Имя")
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name="Планета")
    old = models.IntegerField(verbose_name="Возраст")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"
