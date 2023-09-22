from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import Client, Message, MessageSettings, Logi


#####################   КЛИЕНТЫ РАССЫЛКИ

class ClientCreateView(CreateView):
    model = Client
    fields = ('last_name', 'first_name', 'patronymic', 'comments', 'email', 'year_birth',)
    success_url = reverse_lazy('mailing:client_list')  # ???? адрес для перенаправления


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('last_name', 'first_name', 'patronymic', 'comments', 'email', 'year_birth',)
    success_url = reverse_lazy('mailing:client_list')

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.kwargs.get("uuid"))


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.kwargs.get("uuid"))


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')


# контроллеры для модели  Message
#####################   СООБЩЕНИЕ РАССЫЛКИ

class MessageCreateView(CreateView):
    model = Message
    fields = ('subject_letter', 'body_letter', )
    success_url = reverse_lazy('mailing:message_list')  # ???? адрес для перенаправления


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('subject_letter', 'body_letter',)
    success_url = reverse_lazy('mailing:message_list')

    def get_object(self, queryset=None):
        return Message.objects.get(id=self.kwargs.get("uuid"))

class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message

    def get_object(self, queryset=None):
        return Message.objects.get(id=self.kwargs.get("uuid"))


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')


#####################   РАССЫЛКА

class MessageSettingsCreateView(CreateView):
    model = MessageSettings
    fields = ('name', 'time_from', 'time_by', 'period', 'message', 'status', 'customers', )
    success_url = reverse_lazy('mailing:messagesettings_list')  # ???? адрес для перенаправления


class MessageSettingsListView(ListView):
    model = MessageSettings


class MessageSettingsDetailView(DetailView):
    model = MessageSettings

    def get_object(self, queryset=None):
        return MessageSettings.objects.get(id=self.kwargs.get("uuid"))


class MessageSettingsUpdateView(UpdateView):
    model = MessageSettings
    fields = ('name', 'time_from', 'time_by', 'period', 'message', 'status', 'customers', )
    success_url = reverse_lazy('mailing:messagesettings_list')


    def get_object(self, queryset=None):
        return MessageSettings.objects.get(id=self.kwargs.get("uuid"))


class MessageSettingsDeleteView(DeleteView):
    model = MessageSettings
    success_url = reverse_lazy('mailing:messagesettings_list')


class LogiListView(ListView):
    model = Logi


class LogiCreateView(CreateView):
    model = Logi
    fields = ('message', 'attempt_time_date', 'status', 'server_response', )
    success_url = reverse_lazy('mailing:logi_list')