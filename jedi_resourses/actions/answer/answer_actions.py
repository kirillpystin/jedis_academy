"""Модуль, отвечающий за показ информации об ответах"""
from django.shortcuts import render

from jedi_resourses.models.answer import Answer


class AnswerActions(object):
    """Класс, хранящий действия с ответами кандидатов."""

    @staticmethod
    def show(request, pk, key):
        """Метод, выводящий ответы кандидата.

        Args:
            request (HttpRequest): Запрос.
            pk (str): ключ для поиска кондидата.
            key (str):  ключ для поиска джедая.

        Returns:
            HttpResponse: вывод шаблона с ответами кандидата
        """
        if request.method == "GET":
            questions = (
                Answer.objects.only(
                    "choice", "question", "candidate_id", "candidate__name"
                )
                .filter(candidate__id=key)
                .select_related("candidate")
            )

            return render(
                request,
                "answer/show.html",
                {
                    "answers": {
                        q.question: "Да" if q.choice else "Нет" for q in questions
                    },
                    "candidate": questions.first().candidate,
                    "pk": pk,
                    "key": key,
                },
            )
