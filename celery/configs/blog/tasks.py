from django.core.mail import send_mail
from configs.celery import app

from .service import send



@app.task
def send_spam_email(user_email):
    send(user_email)