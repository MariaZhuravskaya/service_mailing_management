from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('header', 'content', 'image', 'date_creation', 'number_views', 'is_publication',)
