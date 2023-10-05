import uuid

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='id_блога')
    header = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Cодержимое', **NULLABLE)
    image = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='изображение')
    date_creation = models.DateField(auto_now_add=True, verbose_name='дата публикации')
    number_views = models.IntegerField(default=0, verbose_name='количество просмотров')
    is_publication = models.BooleanField(default=True, verbose_name='опубликовано')

    def __str__(self):
        return f"""{self.header}, {self.content}"""

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
