"""Модуль, отвечающий за вывод формы"""
from django import forms

from jedi_resourses.models.jedi import Jedi


class JediForm(forms.ModelForm):
    """Форма входа джедая."""

    class Meta:
        model = Jedi
        fields = ("name",)
