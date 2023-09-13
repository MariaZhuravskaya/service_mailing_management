from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientDeleteView, ClientUpdateView, \
    MessageCreateView, MessageDetailView, MessageListView, MessageUpdateView

app_name = MailingConfig.name


urlpatterns = [
    path('client/create', ClientCreateView.as_view(), name='client_form'),
    path('', ClientListView.as_view(), name='client_list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),


    path('message/create', MessageCreateView.as_view(), name='message_form'),
    path('', MessageListView.as_view(), name='message_list'),
    path('<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>', MessageCreateView.as_view(), name='message_delete'),
]

