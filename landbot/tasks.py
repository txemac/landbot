from celery import shared_task


@shared_task
def send_email_task(message: str):
    # Mock email sending
    print(f"Sending Email: {message}")


@shared_task
def send_slack_task(message: str):
    # Implement Slack API call
    print(f"Sending to Slack: {message}")
