# Generated by Django 4.2.16 on 2024-11-10 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mailing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="clients",
            field=models.ManyToManyField(to="mailing.client", verbose_name="Клиенты"),
        ),
        migrations.AddField(
            model_name="mailing",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mailing.message",
                verbose_name="Письмо",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
        migrations.AddField(
            model_name="logmailing",
            name="mailing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="mailing.mailing",
                verbose_name="Рассылка",
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]