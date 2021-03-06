`Академия джедаев`(прототип приложения по подбору кадров)

Приложение реализует следующие функциональные возможности:
1) Раздельные страницы входа для джедаев и падаванов
2) Регистрацию кандидатов в падаваны
3) Тестовые задания для кандидатов
4) Джедай, при переходе на свою страницу может отобрать кандидатов с его планеты и зачислить в падаваны(но не более трех)
5) Если кандидат отобран в джедаи, то на его почту приходит Email-оповещение
6) Вывод статистики: выведены те джедаи, у которых более 1 падавана

Запуск приложения:
1) Установить `python`. Версия не ниже 3.6. Нужную версию можно загрузить тут: https://www.python.org/downloads/
2) Зайти в корневую папку и создать виртуальное окружение `python3 -m venv virtual_env`
3) Активировать виртуальное окружение `source virtual_env/bin/activate`
4) Установить зависимости `pip install -r requirements.txt`
5) Запустить миграции `python manage.py migrate --run-syncdb`
6) Создать суперпользователя `python manage.py createsuperuser`
7) Запустить локальный сервер `python manage.py runserver`
8) Залогиниться в админке `http://127.0.0.1:8000/admin/`
9) Зарегистрировать орден джедаев, зарегистрировать тесты для данного ордена, добавить тестовые вопросы для тестов.
10) Приложение готово к работе.
