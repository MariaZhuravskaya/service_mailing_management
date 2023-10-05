from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientDeleteView, ClientUpdateView, \
    MessageCreateView, MessageDetailView, MessageListView, MessageUpdateView, MessageSettingsCreateView, \
    MessageSettingsListView, MessageSettingsDetailView, MessageSettingsDeleteView, MessageDeleteView, \
    MessageSettingsUpdateView, LogiListView, LogiCreateView, index

app_name = MailingConfig.name

urlpatterns = [
    path('', cache_page(60)(index)),
    path('message_list', MessageListView.as_view(), name='message_list'),
    path('message/create', MessageCreateView.as_view(), name='message_form'),
    path('message/detail/<uuid:uuid>', MessageDetailView.as_view(), name='message_detail'),
    path('message/<uuid:uuid>', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<uuid:pk>', MessageDeleteView.as_view(), name='message_delete'),

    path('messagesettings_list', MessageSettingsListView.as_view(), name='messagesettings_list'),
    path('messagesettings/create', MessageSettingsCreateView.as_view(), name='messagesettings_form'),
    path('messagesettings/detail/<uuid:uuid>', MessageSettingsDetailView.as_view(), name='messagesettings_detail'),
    path('messagesettings/<uuid:uuid>', MessageSettingsUpdateView.as_view(), name='messagesettings_update'),
    path('messagesettings/delete/<uuid:pk>', MessageSettingsDeleteView.as_view(), name='messagesettings_delete'),

    path('client_list', ClientListView.as_view(), name='client_list'),
    path('client/create', ClientCreateView.as_view(), name='client_form'),
    path('client/detail/<uuid:uuid>', ClientDetailView.as_view(), name='client_detail'),
    path('client/<uuid:uuid>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<uuid:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('logi_list', LogiListView.as_view(), name='logi_list'),
    path('logi/create', LogiCreateView.as_view(), name='logi_form'),
]
