"""Модуль, отвечающий за отправку электронной почты"""
import os

from django.contrib import messages
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send(request, email):
    """Функция, отпраляющая email на адрес кандидата.

    Args:
        request(django.core.handlers.wsgi.WSGIRequest): Запрос.
        email(str): Адрес электронной почты.

    Returns:
        None or сообщение об ошибке.
    """
    try:
        SendGridAPIClient(os.environ.get("SENDGRID_API_KEY")).send(
            Mail(
                from_email="kpystin123@gmail.com",
                to_emails=email,
                subject="Вы приняты в академию джедаев",
                html_content="<strong>Поздравляем, отныне Вы падаван</strong>",
            )
        )
    except Exception:
        return messages.error(request, "Сообщение не доставлено.")
