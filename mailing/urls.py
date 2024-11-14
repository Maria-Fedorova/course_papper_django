from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    MailingCreateView, MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView, \
    IndexListView, ContactsView, activity

app_name = MailingConfig.name

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path('contacts/', ContactsView.as_view, name='contacts'),

    path("client/", ClientListView.as_view(), name="client_list"),
    path("client/create/", ClientCreateView.as_view(), name="client_create"),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("client/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),

    path("message/", MessageListView.as_view(), name="message_list"),
    path("message/create/", MessageCreateView.as_view(), name="message_create"),
    path("message/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),

    path("mailing/", MailingListView.as_view(), name="mailing_list"),
    path("mailing/create/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing/<int:pk>/update/", MailingUpdateView.as_view(), name="mailing_update"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"),
    path('mailing/activity/<int:pk>/', activity, name='activity'),

]
