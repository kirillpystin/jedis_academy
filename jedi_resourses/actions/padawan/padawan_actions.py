"""Модуль, отвечающий за создание падавана"""
from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from jedi_resourses.actions.email.send import send
from jedi_resourses.models.padawan import Padawan


class PadawanActions(object):
    """Класс, хранящий действия над падаванами."""

    @csrf_exempt
    def add_to_padawan(request, pk):
        """Метод добавления в падаваны.

        Если у джедая уже есть 3 подавана,
        то выводится сообщение об ошибке.

        Args:
            pk (str): Ключ для записей джедая.

        Returns:
            HttpResponse: Ответ с шаблоном для вывода страницы джедая для выбора кандидатов.
        """
        LIMIT = 3
        if request.method == "POST":
            key = request.POST.get("key")
            all_padawans = Padawan.objects.filter(jedi_id=key)
            if all_padawans.count() < LIMIT:
                padawan = Padawan(jedi_id=key, candidate_id=pk)
                email = padawan.candidate.email
                padawan.save()
                send(request, email)
            else:
                messages.success(
                    request, "Достигнут лимит возможного количества падаванов"
                )

            return redirect(f"/jedi_page/{key}")
