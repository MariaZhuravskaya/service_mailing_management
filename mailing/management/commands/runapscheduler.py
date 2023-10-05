import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore  # ThreadPoolExecutor
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from datetime import datetime, date, timedelta
from django.conf import settings
from django.core.mail import send_mail
import smtplib

smtplib.SMTP.debuglevel = 9

# Кастомная команда
# Вызывать команду необходимо через всё тот же файл обслуживания фреймворка
# manage.py
# Сама команда должна обязательно наследоваться от базового класса и реализовывать обязательный метод handle


logger = logging.getLogger(__name__)


def my_job():
    # Your job processing logic here...
    from mailing.models import MessageSettings, Logi
    settings_all = MessageSettings.objects.all()
    for meiling in settings_all:

        if can_send(meiling):
            print('Skip send email for ' + str(meiling.id))
            continue

        else:

            now = datetime.now()
            from_t = datetime.combine(meiling.time_from.date(), meiling.time_from.time())
            to_t = datetime.combine(meiling.time_by.date(), meiling.time_by.time())

            if from_t < now < to_t:

                meiling.status = 'запущена'
                meiling.last_dispatch_date = date.today()
                meiling.save()

                for client in meiling.customers.all():
                    try:
                        print('Sending email for ' + client.email)
                        result = send_mail(meiling.message.subject_letter, meiling.message.body_letter,
                                           settings.EMAIL_HOST_USER,
                                           [client.email])

                        today = date.today()

                        if today >= meiling.time_by.date():
                            meiling.status = 'завершена'
                            meiling.save()

                        log = Logi.objects.create(
                            status='Успешная отправка рассылки',
                            attempt_time_date=datetime.now(),
                            server_response="OK",
                            message=meiling)
                        log.save()



                    except smtplib.SMTPException:
                        log = Logi.objects.create(status='Рассылка не отправлена. Повторите попытку позже',
                                                  attempt_time_date=datetime.now(),
                                                  server_response='Error',
                                                  message=meiling
                                                  )
                        log.save()

            else:
                continue



def can_send(m):
    today = date.today()
    if m.last_dispatch_date is None:
        return False
    if m.period == 'Каждый день':
        return m.last_dispatch_date == today
    elif m.period == 'Каждую неделю':
        start_week = today - timedelta(today.weekday())
        end_week = start_week + timedelta(7)
        return start_week <= m.last_dispatch_date <= end_week
    elif m.period == 'Каждый месяц':
        monthly = datetime.now().month
        year = datetime.now().year

        monthly_m = m.last_dispatch_date.month
        year_m = m.last_dispatch_date.year

        return monthly_m == monthly and year_m == year

    else:
        raise Exception('Нет такого периода рассылки')


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    Этот метод удаляет из базы данных записи о выполнении задания APScheduler старше `max_age`.
    Это помогает предотвратить заполнение базы данных старыми историческими записями, которые больше
    не являются полезными.

    :param max_age: максимальный период времени для сохранения исторических записей о выполнении задания.
     Значение по умолчанию - 7 дней.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(
                hour="9", minute="00"
            ),  # Запустить задачу каждый день в 9:00
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
