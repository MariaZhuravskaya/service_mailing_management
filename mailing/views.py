from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.models import Client, Message


class ClientCreateView(CreateView):
    model = Client
    fields = ('last_name', 'first_name', 'patronymic', 'comments', 'email', )
    success_url = reverse_lazy('client:list')        # ???? адрес для перенаправления


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('last_name', 'first_name', 'patronymic', 'comments', 'email', 'year_birth', )
    success_url = reverse_lazy('client:list')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:list')


# контроллеры для модели  Message

class MessageCreateView(CreateView):
    model = Message
    fields = ('subject_letter', 'body_letter', 'client', 'message_sattings',)
    success_url = reverse_lazy('client:list')        # ???? адрес для перенаправления


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('subject_letter', 'body_letter', 'client', 'message_sattings',)
    success_url = reverse_lazy('message:list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('message:list')
