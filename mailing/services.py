import smtplib
from datetime import datetime

import pytz
from django.core.mail import send_mail

from config.settings import CACHE_ENABLED
from django.core.cache import cache
from django.conf import settings

from mailing.models import Mailing, LogMailing


def get_mailing_from_cache():
    if CACHE_ENABLED:
        key = "mailings_count"
        mailings_count = cache.get(key)
        if mailings_count is None:
            mailings_count = Mailing.objects.all().count()
            cache.set(key, mailings_count)
    else:
        mailings_count = Mailing.objects.all().count()
    return mailings_count


def send_mailing(mailing):
    emailing_list = [client.email for client in mailing.clients.all()]
    try:
        response_server = send_mail(
            topic=mailing.message.topic,
            message=mailing.message.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=emails_list,
            fail_silently=False,
        )
        log = LogMailing.objects.create(mailing=mailing, status=True, response=response_server)
        log.save()
    except smtplib.SMTPException as e:
        log = LogMailing.objects.create(mailing=mailing, status=False, response=e)
        log.save()


def start_mailing():
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(is_active=True).filter(status_mailing__in=["создана", "запущена"])

    for mailing in mailings:
        log = LogMailing.objects.filter(mailing=mailing).order_by("-last_mailing").first()
        passed_time = (current_datetime - log.last_mailing).days
        if log:
            if current_datetime > log.last_mailing:
                match mailing.period:
                    case "раз в день":
                        if passed_time >= 1:
                            send_mailing(mailing)
                    case "раз в неделю":
                        if passed_time >= 7:
                            send_mailing(mailing)
                    case "раз в месяц":
                        if passed_time >= 30:
                            send_mailing(mailing)
            mailing.status_mailing = "завершена"
        else:
            send_mailing(mailing)
            mailing.status_mailing = "запущена"
            mailing.save()
