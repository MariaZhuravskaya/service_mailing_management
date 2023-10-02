from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import Client, Message, MessageSettings, Logi


#####################   КЛИЕНТЫ РАССЫЛКИ

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('last_name', 'first_name', 'patronymic', 'comments', 'email', 'year_birth',)
    success_url = reverse_lazy('mailing:client_list')  # ???? адрес для перенаправления

    def form_valid(self, form):
        self.object = form.save()
        self.object.client_user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Client
    permission_required = 'mailing.change_client'
    fields = ('last_name', 'first_name', 'patronymic', 'comments', 'email', 'year_birth',)
    success_url = reverse_lazy('mailing:client_list')

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.kwargs.get("uuid"))


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.kwargs.get("uuid"))


class ClientDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Client
    permission_required = 'mailing.delete_client'
    success_url = reverse_lazy('mailing:client_list')


# контроллеры для модели  Message
#####################   СООБЩЕНИЕ РАССЫЛКИ

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ('subject_letter', 'body_letter', )
    success_url = reverse_lazy('mailing:message_list')  # ???? адрес для перенаправления


class MessageUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Message
    fields = ('subject_letter', 'body_letter',)
    permission_required = 'mailing.change_message'
    success_url = reverse_lazy('mailing:message_list')

    def get_object(self, queryset=None):
        return Message.objects.get(id=self.kwargs.get("uuid"))

class MessageListView(ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

    def get_object(self, queryset=None):
        return Message.objects.get(id=self.kwargs.get("uuid"))


class MessageDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Message
    permission_required = 'mailing.delete_message'
    success_url = reverse_lazy('mailing:message_list')


#####################   РАССЫЛКА

class MessageSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MessageSettings
    fields = ('name', 'time_from', 'time_by', 'period', 'message', 'status', 'customers', )
    success_url = reverse_lazy('mailing:messagesettings_list')  # ???? адрес для перенаправления


class MessageSettingsListView(LoginRequiredMixin, ListView):
    model = MessageSettings


class MessageSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MessageSettings

    def get_object(self, queryset=None):
        return MessageSettings.objects.get(id=self.kwargs.get("uuid"))


class MessageSettingsUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = MessageSettings
    permission_required = 'mailing.change_messagesettings'
    fields = ('name', 'time_from', 'time_by', 'period', 'message', 'status', 'customers', )
    success_url = reverse_lazy('mailing:messagesettings_list')


    def get_object(self, queryset=None):
        return MessageSettings.objects.get(id=self.kwargs.get("uuid"))


class MessageSettingsDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = MessageSettings
    permission_required = 'mailing.delete_messagesettings'
    success_url = reverse_lazy('mailing:messagesettings_list')


class LogiListView(LoginRequiredMixin, ListView):
    model = Logi


class LogiCreateView(LoginRequiredMixin, CreateView):
    model = Logi
    fields = ('message', 'attempt_time_date', 'status', 'server_response', )
    success_url = reverse_lazy('mailing:logi_list')