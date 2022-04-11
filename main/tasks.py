from send_email.celery import app

from .service import send


@app.task
def send_spam_email(user_email, user_name):
    send(user_email, user_name)
