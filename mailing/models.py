import uuid

from django.db import models


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
    #client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент')
    #message_sattings = models.ForeignKey(MessageSattings, on_delete=models.CASCADE, verbose_name='настройки рассылки')

    def __str__(self):
        return f'{self.subject_letter}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class MessageSattings(models.Model):
    time_from = models.DateTimeField(verbose_name='Дата и время запуска рассылки')
    time_by = models.DateTimeField(verbose_name='Дата и время окончания рассылки')
    status = models.CharField(verbose_name="статус рассылки")
    frequency = models.DateTimeField(verbose_name="периодичность")
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.status}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'


#
# class Logi(models.Model):
#     attempt_time_date = models.DateTimeField(auto_now=True, verbose_name='время последней попытки')
#     status = models.CharField(verbose_name="статус попытки")
#     server_response = models.CharField(verbose_name="ответ сервера")
#
#     def __str__(self):
#         return f'{self.status}'
#
#     class Meta:
#         verbose_name = 'лог рассылки'
#         verbose_name_plural = 'логи рассылки'
#
