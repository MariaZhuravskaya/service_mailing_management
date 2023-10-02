from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
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


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('last_name', 'first_name', 'patronymic', 'comments', 'email', 'year_birth',)
    success_url = reverse_lazy('mailing:client_list')

    def get_object(self, queryset=None):
        self.object = Client.objects.get(id=self.kwargs.get("uuid"))
        if self.object.client_user != self.request.user:
            raise Http404
        return self.object


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_object(self, queryset=None):
        return Client.objects.get(id=self.kwargs.get("uuid"))


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailing:client_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get("pk"), client_user=self.request.user)
        return queryset


# контроллеры для модели  Message
#####################   СООБЩЕНИЕ РАССЫЛКИ

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ('subject_letter', 'body_letter', )
    success_url = reverse_lazy('mailing:message_list')  # ???? адрес для перенаправления


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Message
    fields = ('subject_letter', 'body_letter',)
    permission_required = 'mailing.change_message'
    success_url = reverse_lazy('mailing:message_list')

    def get_object(self, queryset=None):
        self.object = Client.objects.get(id=self.kwargs.get("uuid"))
        if self.object.client_user != self.request.user:
            raise Http404
        return self.object
    #
    # def get_object(self, queryset=None):
    #     return Message.objects.get(id=self.kwargs.get("uuid"))

class MessageListView(ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

    def get_object(self, queryset=None):
        return Message.objects.get(id=self.kwargs.get("uuid"))


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get("pk"), client_user=self.request.user)
        return queryset


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


class MessageSettingsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MessageSettings
    permission_required = 'mailing.change_messagesettings'
    fields = ('name', 'time_from', 'time_by', 'period', 'message', 'status', 'customers', )
    success_url = reverse_lazy('mailing:messagesettings_list')

    def get_object(self, queryset=None):
        self.object = Client.objects.get(id=self.kwargs.get("uuid"))
        if self.object.client_user != self.request.user:
            raise Http404
        return self.object

    # def get_object(self, queryset=None):
    #     return MessageSettings.objects.get(id=self.kwargs.get("uuid"))


class MessageSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MessageSettings
    success_url = reverse_lazy('mailing:messagesettings_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get("pk"), client_user=self.request.user)
        return queryset


class LogiListView(LoginRequiredMixin, ListView):
    model = Logi


class LogiCreateView(LoginRequiredMixin, CreateView):
    model = Logi
    fields = ('message', 'attempt_time_date', 'status', 'server_response', )
    success_url = reverse_lazy('mailing:logi_list')