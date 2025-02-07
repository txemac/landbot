from celery import shared_task
from django.core.mail import send_mail
from landbot.settings import DEFAULT_FROM_EMAIL
from landbot.settings import RECIPIENT_LIST


@shared_task
def send_email_task(message: str):
    send_mail(
        subject="New notification",
        message=message,
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=RECIPIENT_LIST,
        fail_silently=False,
    )
    print(f"Sending Email: {message}")


@shared_task
def send_slack_task(message: str):
    # Implement Slack API call
    print(f"Sending to Slack: {message}")
