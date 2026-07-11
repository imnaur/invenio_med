from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from .models import Appointment


@shared_task
def send_appointment_email_task(
    patient_name, patient_email, patient_phone, appointment_date_str
):
    message_body = (
        f"Пользователь {patient_name}\n"
        f"Email пациента {patient_email}\n"
        f"Телефон пациента {patient_phone}\n"
        f"Дата и время приема {appointment_date_str}"
    )

    send_mail(
        subject="Новая заявка с сайта ожидает подтверждения",
        message=message_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=["imnaur@bk.ru"],
        fail_silently=False,
    )

@shared_task
def check_upcoming_appointments():
    tomorrow = timezone.now() + timedelta(days=1)
    upcoming = Appointment.objects.filter(date__date=tomorrow.date())

    for app in upcoming:
        send_appointment_email_task.delay(
            patient_name=f"{app.patient.first_name} {app.patient.last_name}",
            patient_email=app.patient.email,
            patient_phone=str(app.patient.phone_number),
            appointment_date_str=app.date.strftime("%d.%m.%Y в %H:%M"),
        )
