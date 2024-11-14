from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="Почта")
    last_name = models.CharField(max_length=50, **NULLABLE, verbose_name="Фамилия")
    first_name = models.CharField(max_length=50, **NULLABLE, verbose_name="Имя")
    middle_name = models.CharField(max_length=50, **NULLABLE, verbose_name="Отчество")
    comment = models.TextField(**NULLABLE, verbose_name="Комментарий")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return (f"Почта: {self.email} "
                f"Фамилия: {self.last_name} "
                f"Имя: {self.first_name} "
                f"Отчество: {self.middle_name} "
                f"Почта: {self.email} ")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Mailing(models.Model):
    PERIOD = [
        ("Раз в день", "раз в день"),
        ("Раз в неделю", "раз в неделю"),
        ("Раз в месяц", "раз в месяц"),
    ]
    STATUS = [
        ("создана", "создана"),
        ("запущена", "запущена"),
        ('завершена', 'завершена'),
    ]
    name = models.CharField(unique=True, max_length=255, verbose_name="Тема рассылки")
    clients = models.ManyToManyField("Client", verbose_name="Клиенты")
    message = models.ForeignKey("Message", on_delete=models.CASCADE, verbose_name="Письмо")
    launch_at = models.DateTimeField(default=timezone.now, verbose_name="Дата и время начала рассылки")
    period = models.CharField(max_length=15, choices=PERIOD, verbose_name="Периодичность рассылки")
    status = models.CharField(default="создана", max_length=10, choices=STATUS, verbose_name="Статус рассылки")
    is_active = models.BooleanField(default=True, verbose_name="Активная рассылка")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.name}: Дата начала: {self.launch_at}. Статус: {self.status}'

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ('deactivate', 'Can deactivate mailing'),
            ('view_all', 'Can view all mailings'),
        ]


class Message(models.Model):
    topic = models.CharField(max_length=255, verbose_name="Тема письма")
    body = models.TextField(**NULLABLE, verbose_name="Тело сообщения")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f"{self.topic}: {self.body}"

    class Meta:
        verbose_name = "Письмо"
        verbose_name_plural = "Письма"


class LogMailing(models.Model):
    """Модель лога"""
    mailing = models.ForeignKey("Mailing", on_delete=models.CASCADE, **NULLABLE, verbose_name="Рассылка")
    last_mailing = models.DateTimeField(auto_now=True, verbose_name="Дата и время последней попытки")
    status = models.BooleanField(max_length=10, default=False, verbose_name="Статус попытки")
    response = models.TextField(**NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        return (f"{self.mailing}: Дата и время последней попытки({self.last_mailing})\n"
                f"Статус попытки{self.status}\n"
                f"Ответ сервера{self.response}")

    class Meta:
        verbose_name = 'Логирование'
        verbose_name_plural = 'Логирования'
