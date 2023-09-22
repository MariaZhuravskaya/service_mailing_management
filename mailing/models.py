import uuid
from enum import Enum

from django.apps import apps
from django.db import models
from django.dispatch import receiver
from datetime import datetime, date

from mailing.apps import MailingConfig
#from mailing.mail_sender import send_mails

NULLBOL = {'blank': True, 'null': True}


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='id_клиента')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    comments = models.TextField(**NULLBOL, verbose_name='комментарии')
    year_birth = models.DateField(verbose_name='год рождения')
    email = models.EmailField(verbose_name='почта', unique=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='id_сообщения')
    subject_letter = models.CharField(max_length=50, verbose_name='тема письма')
    body_letter = models.TextField(**NULLBOL, verbose_name='тело письма')

    def __str__(self):
        return f'{self.subject_letter}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MessageSettings(models.Model):

    class Period(models.TextChoices):
        dayly = "Каждый день"
        weekly = "Каждую неделю"
        monthly = "Каждый месяц"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='id_рассылки')
    name = models.CharField(max_length=50, verbose_name="наименование рассылки")
    time_from = models.DateTimeField(verbose_name='Дата и время запуска рассылки')
    time_by = models.DateTimeField(verbose_name='Дата и время окончания рассылки')
    period = models.CharField(max_length=50, choices=Period.choices, verbose_name="Период рассылки")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Письмо для рассылки")
    customers = models.ManyToManyField(Client, verbose_name="Список клиентов")
    status = models.CharField(max_length=50, default='создана', verbose_name="Статус рассылки")
    last_dispatch_date = models.DateField(**NULLBOL, verbose_name='дата последней отправки')

    def __str__(self):
        return f'{self.status}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'



class Logi(models.Model):
    message = models.ForeignKey(MessageSettings, on_delete=models.CASCADE, verbose_name='ID рассылки')
    attempt_time_date = models.DateTimeField(auto_now=True, verbose_name='время последней попытки')
    status = models.CharField(max_length=150, verbose_name="статус попытки")        # Статус - успешно доставлено, в очереди на отправку, ошибка отправки. Как вариант.
    server_response = models.CharField(max_length=150, verbose_name="ответ сервера", **NULLBOL)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        verbose_name = 'лог рассылки'
        verbose_name_plural = 'логи рассылки'
