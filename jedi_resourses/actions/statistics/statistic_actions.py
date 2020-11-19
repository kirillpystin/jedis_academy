"""Модуль, отвечающий за вывод статистики"""
from django.db.models import Count
from django.shortcuts import render

from jedi_resourses.models.padawan import Padawan


class StatisticsActions(object):
    """Класс для действий с статистикой."""

    def get_statistics(request):
        """Метод,отвечающий за вывод статистики.

        Returns:
            HttpResponse: Ответ на запрос.
        """
        return render(
            request,
            "statistics/show.html",
            {
                "jedis": Padawan.objects.values(
                    "jedi_id", "jedi__name", "jedi__planet__name"
                )
                .annotate(count_padawan=Count("jedi_id"))
                .order_by("jedi__name")
            },
        )
