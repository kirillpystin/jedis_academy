"""Модуль, отвечающий за создание класса `Answer`"""
from django.db import models

from .candidate import Candidate
from .question import Question


class Answer(models.Model):
    """Класс, используемый для сохранения ответов кандидатов.

    Attributes:
        question (Question): Ссылка на вопрос, к которому дан ответ.
        choice (bool): Ссыллка на вопрос, к которому дан ответ.
        candidate (Candidate): Кандидат, ответивший на вопрос.

    """

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="Вопрос"
    )
    choice = models.BooleanField(verbose_name="Ответ")
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, verbose_name="Кандидат"
    )

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    __slots__ = ("question", "choice", "candidate")
