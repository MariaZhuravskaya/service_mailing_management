
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLOBOL = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLOBOL)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLOBOL)
    cantry = models.CharField(max_length=50, verbose_name='страна', **NULLOBOL)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    id = models.IntegerField(primary_key=True, default=0, editable=False, verbose_name='id_клиента')
    is_active = models.BooleanField(default=False)
