"""Модуль, отвечающий за создание класса `Padawan`"""
from django.db import models

from .candidate import Candidate
from .jedi import Jedi


class Padawan(models.Model):
    """Класс, отвечающий за регистрацию падаванов.

    Attributes:
        jedi(Jedi): Джедай, который является наставником падавана.
        candidate(Candidate): Кандидат, который стал падаваном.
    """

    jedi = models.ForeignKey(Jedi, on_delete=models.CASCADE, verbose_name="Джедай")
    candidate = models.OneToOneField(
        Candidate, on_delete=models.CASCADE, verbose_name="Кандидат"
    )

    class Meta:
        verbose_name = "Падаван"
        verbose_name_plural = "Падаваны"

    __slots__ = ("jedi", "candidate")
