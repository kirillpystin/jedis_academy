"""Модуль, отвечающий за регистрацию кандидата"""
from django.shortcuts import redirect, render

from jedi_resourses.forms.candidate.form import CandidateForm
from jedi_resourses.models.planet import Planet


class CandidateActions(object):
    """Класс, хранящий действия над объектами кандидатов."""

    @staticmethod
    def new_candidate(request):
        """Метод, создающий нового кандидата.

        После создания кандидата осуществляется перенаправление
        на страницу с тестом для данного кандидата.

        Args:
            request (HTTPRequest): запрос.

        Returns:
            HttpResponse: шаблон для регистрации в кандидатах
        """
        if request.method == "POST" and CandidateForm(request.POST).is_valid():
            return redirect("/test/%d" % CandidateForm(request.POST).save().id)

        return render(
            request,
            "candidate/create.html",
            {"form": CandidateForm, "planets": Planet.objects.only("name")},
        )
