from api.factory.base import NotificationFactory
from landbot.tasks import send_email_task


class EmailNotificationFactory(NotificationFactory):

    NAME = "Email"

    def send_notification(
        self,
        message: str,
    ) -> bool:
        send_email_task.delay(message=message)
        return True
