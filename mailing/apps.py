from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'
    verbose_name = 'Рассылка'
    scheduler = None

    # def ready(self):
    #     from . import jobs
    #     self.scheduler = jobs.configure()
