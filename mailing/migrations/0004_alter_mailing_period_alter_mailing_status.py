# Generated by Django 4.2.16 on 2024-11-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_alter_mailing_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="period",
            field=models.CharField(
                choices=[
                    ("daily", "Once a day"),
                    ("weekly", "Once a week"),
                    ("monthly", "Once a month"),
                ],
                max_length=15,
                verbose_name="Периодичность рассылки",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Created"),
                    ("launched", "Launched"),
                    ("completed", "Completed"),
                ],
                default="создана",
                max_length=10,
                verbose_name="Статус рассылки",
            ),
        ),
    ]
