from django.contrib import admin

from mailing.models import Client, Message, Mailing, LogMailing


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "last_name", "first_name", "middle_name", "comment", "owner",)
    list_filter = ("owner",)
    search_fields = ("email", "last_name", "owner",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "message", "launch_at", "period", "status", "owner",)
    list_filter = ("name", "launch_at", "period", "status",)
    search_fields = ("name", "launch_at", "message", "period", "status",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("pk", "topic", "body", "owner",)
    search_fields = ("topic", "owner",)


@admin.register(LogMailing)
class LoggingMailingAdmin(admin.ModelAdmin):
    list_display = ("pk", "mailing", "last_mailing", "status", "response",)
    list_filter = ("last_mailing", "status",)
