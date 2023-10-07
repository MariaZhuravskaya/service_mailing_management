from random import random

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog
from mailing.forms import MessageSettingsForm
from mailing.models import Client, Message, MessageSettings, Logi


def index(request):
    if request.method == 'GET':
        context = {
            'count_total': len(MessageSettings.objects.all()),
            'count': len(MessageSettings.objects.filter(status="запущена")) + len(
                MessageSettings.objects.filter(status="создана")),
            'client': len(Client.objects.all()),
            'blog': Blog.objects.order_by('?')[:3]
        }

        return render(request, 'mailing/index.html', context)


#####################   КЛИЕНТЫ РАССЫЛКИ

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ('last_name', 'first_name', 'patronymic', 'comments', 'email', 'year_birth',)
    success_url = reverse_lazy('mailing:client_list')

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
    fields = ('subject_letter', 'body_letter',)
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.message_user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ('subject_letter', 'body_letter',)
    success_url = reverse_lazy('mailing:message_list')

    def get_object(self, queryset=None):
        self.object = Message.objects.get(id=self.kwargs.get("uuid"))
        if self.object.message_user != self.request.user:
            raise Http404
        return self.object


class MessageListView(LoginRequiredMixin, ListView):
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
        queryset = queryset.filter(id=self.kwargs.get("pk"), message_user=self.request.user)
        return queryset


#####################   РАССЫЛКА

class MessageSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MessageSettings
    form_class = MessageSettingsForm
    success_url = reverse_lazy('mailing:messagesettings_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.message_settings_user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'uuid': self.request.user.id})
        return kwargs


class MessageSettingsListView(LoginRequiredMixin, ListView):
    model = MessageSettings

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.all()
        return queryset


class MessageSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MessageSettings

    def get_object(self, queryset=None):
        return MessageSettings.objects.get(id=self.kwargs.get("uuid"))


class MessageSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MessageSettings
    fields = ('name', 'time_from', 'time_by', 'period', 'message', 'status', 'customers',)
    success_url = reverse_lazy('mailing:messagesettings_list')

    def get_object(self, queryset=None):
        self.object = MessageSettings.objects.get(id=self.kwargs.get("uuid"))
        if self.object.message_settings_user != self.request.user:
            raise Http404
        return self.object


class MessageSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MessageSettings
    success_url = reverse_lazy('mailing:messagesettings_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get("pk"), message_settings_user=self.request.user)
        return queryset


class LogiListView(LoginRequiredMixin, ListView):
    model = Logi


class LogiCreateView(LoginRequiredMixin, CreateView):
    model = Logi
    fields = ('message', 'attempt_time_date', 'status', 'server_response',)
    success_url = reverse_lazy('mailing:logi_list')
