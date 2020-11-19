"""Модуль, отвечающий за вывод формы"""
from django import forms

from jedi_resourses.models.candidate import Candidate


class CandidateForm(forms.ModelForm):
    """Форма регистации кандидата."""

    class Meta:
        model = Candidate
        fields = ("name", "old", "planet", "email")
