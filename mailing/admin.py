from django.contrib import admin

from mailing.models import Client, Message, MessageSettings, Logi



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'patronymic', 'comments', 'email', 'year_birth', )
    list_filter = ('year_birth',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_letter', 'body_letter', )


@admin.action(description="Отметить выбранные рассылки как завершенные")
def make_status(self, request, queryset):
    queryset.update(status="завершена")


class MessageSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_from', 'time_by', 'period', 'message', 'status', )
    list_filter = ('name', 'status',)
    actions = [make_status]


admin.site.register(MessageSettings, MessageSettingsAdmin)

@admin.register(Logi)
class LogiAdmin(admin.ModelAdmin):
    fields = ('message', 'status', 'server_response', )
    list_filter = ('status',)
