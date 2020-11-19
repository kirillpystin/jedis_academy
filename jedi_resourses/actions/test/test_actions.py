"""Модуль, отвечающий за тесты для кандидатов"""
import random

from django.shortcuts import redirect, render

from jedi_resourses.admin import Answer, Candidate, Question, Test


class TestActions(object):
    def test(request, pk):
        """Метод, отвечающий за обработку ответов на вопросы тестового задания.

        Args:
            pk (str): ключ для записи кандидата.

        Returns:
            HttpResponse: ответ с шаблоном для вывода страницы с результатом тестов.
        """
        random_test = random.choice(Test.objects.all())
        questions = Question.objects.filter(test=random_test)
        if request.method == "POST":
            array = dict(
                zip(request.POST.getlist("question"), request.POST.getlist("polls"))
            )
            for question_id, poll in iter(array.items()):
                answer = Answer(question_id=question_id, choice=poll, candidate_id=pk)
                answer.save()
            return redirect("/new/")
        return render(request, "test/show.html", {"questions": questions, "pk": pk})
