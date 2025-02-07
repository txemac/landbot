from api.factory.base import NotificationFactory
from landbot.tasks import send_slack_task


class SlackNotificationFactory(NotificationFactory):

    NAME = "Slack"

    def send_notification(
        self,
        message: str,
    ) -> bool:
        send_slack_task.delay(message=message)
        return True
