"""Модуль, отвечающий за тесты"""
from django.db import models


class Test(models.Model):
    """Класс, отвечающий за создание уникальных тестов.

    Attributes:
        orden(UUIDField): Уникальный код ордена.

    """

    orden = models.UUIDField(verbose_name="Код ордена", unique=True)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    __slots__ = ("orden",)
