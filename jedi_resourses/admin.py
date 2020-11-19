"""Модуль, отвечающий за регистрацию классов в админке"""

from django.contrib import admin

from .models.answer import Answer
from .models.candidate import Candidate
from .models.jedi import Jedi
from .models.padawan import Padawan
from .models.planet import Planet
from .models.question import Question
from .models.test import Test

admin.site.register(Planet)
admin.site.register(Jedi)
admin.site.register(Candidate)
admin.site.register(Test)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Padawan)
