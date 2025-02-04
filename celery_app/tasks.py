from celery import shared_task
from time import sleep 
from django.core.mail import send_mail

@shared_task
def sleepy():
    return "celery executed"

@shared_task
def send_email():
    send_mail("Celery worked!",
              "proof that celery worked",
              "gautamggn13@gmail.com",
              ["sopede9773@kuandika.com"])
    return None