from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from jedi_resourses.forms.jedi.form import JediForm
from jedi_resourses.models.candidate import Candidate
from jedi_resourses.models.jedi import Jedi
from jedi_resourses.models.padawan import Padawan


class JediActions(object):
    """Класс, хранящий действия с джедаями."""

    @staticmethod
    @csrf_exempt
    def get_jedi_page(request):
        """Метод, используемая для перенаправки на страницу с кандидатами.

        Args:
            request(django.core.handlers.wsgi.WSGIRequest): Запрос.

        Returns:
            HttpResponsePermanentRedirect: Перенаправление на целевую страницу.
        """
        if request.method == "POST":
            return redirect(f"/jedi_page/{int(request.POST.get('id'))}")

    @staticmethod
    def select_jedi(request):
        """Метод, предоставляющая шаблон выбора джедая.

        Args:
            request(django.core.handlers.wsgi.WSGIRequest): Запрос.

        Returns:
            HttpResponsePermanentRedirect: Перенаправление на целевую страницу.
        """
        return render(
            request,
            "jedi/select.html",
            {"form": JediForm, "jedis": Jedi.objects.only("name")},
        )

    @staticmethod
    def jedi_page(request, pk):
        """Метод, выводящий информацию на страницу джедая.

        Args:
            pk (str): ключ для записей джедаев

        Returns:
            HttpResponse: ответ с шаблоном для вывода страницы джедая для выбора кандидатов
        """
        jedi = get_object_or_404(Jedi, id=pk)
        if request.method == "GET":
            return render(
                request,
                "jedi/show.html",
                {
                    "candidates": (
                        Candidate.objects.filter(planet=jedi.planet).exclude(
                            id__in=tuple(
                                Padawan.objects.values_list("candidate_id", flat=True)
                            )
                        )
                    ),
                    "pk": pk,
                },
            )
