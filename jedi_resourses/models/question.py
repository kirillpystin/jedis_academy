"""Модуль, отвечающий за создание класса `Question`"""
from django.db import models

from .test import Test


class Question(models.Model):
    """Класс, используемы ждя сохранения вопросов к тестам.

    Attributes:
        text(CharField): Текст вопроса.
        test(Test): Cсылка на тест, к которому относится вопрос.
    """

    text = models.CharField(max_length=200, verbose_name="Вопрос")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text

    __slots__ = ("text", "test")
