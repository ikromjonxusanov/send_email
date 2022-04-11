from django.conf import settings
from django.core.mail import send_mail

from send_email.celery import app
from .models import Contact

from .service import send


@app.task
def send_message_email(user_email, user_name):
    send(user_email, user_name)


@app.task
def send_beat_email():
    for con in Contact.objects.all():
        send_mail(
            f"Hi {con.name}!!!",
            "You will receive a message every 5 minutes",
            settings.EMAIL_HOST,
            [con.email],
            fail_silently=False
        )
