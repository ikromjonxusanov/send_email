from django.conf import settings
from django.core.mail import send_mail


def send(user_email, user_name):
    send_mail(
        f"Hi {user_name}!!!",
        "You have been notified",
        settings.EMAIL_HOST,
        [user_email],
        fail_silently=False
    )
