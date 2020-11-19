"""Модуль, отвечающий за роутинг"""
from django.conf.urls import url

from .actions.answer.answer_actions import AnswerActions
from .actions.candidate.candidate_actions import CandidateActions
from .actions.jedi.jedi_actions import JediActions
from .actions.padawan.padawan_actions import PadawanActions
from .actions.statistics.statistic_actions import StatisticsActions
from .actions.test.test_actions import TestActions

urlpatterns = [
    url(r"^$", CandidateActions.new_candidate),
    url(r"^new/$", CandidateActions.new_candidate, name="new"),
    url(r"^jedi/$", JediActions.select_jedi, name="jedi"),
    url(r"^get_jedi_page/$", JediActions.get_jedi_page, name="get_jedi_page"),
    url(r"^jedi_page/(?P<pk>\d+)$", JediActions.jedi_page, name="jedi_page"),
    url(r"^test/(?P<pk>\d+)$", TestActions.test, name="test"),
    url(r"^detail/(?P<pk>\d+)/(?P<key>\d+)", AnswerActions.show, name="detail"),
    url(r"^add_to_padawan/(?P<pk>\d+)", PadawanActions.add_to_padawan, name="add"),
    url(r"^statistic/", StatisticsActions.get_statistics, name="statistics"),
]
