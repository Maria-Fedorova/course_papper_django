# Generated by Django 4.2.16 on 2024-11-14 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ("email",),
                "permissions": [
                    ("deactivate", "Can deactivate user"),
                    ("view_all", "Can view all users"),
                ],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
