from api.factory.base import NotificationFactory


class SlackNotificationFactory(NotificationFactory):

    NAME = "Slack"

    def send_notification(
        self,
        message: str,
    ) -> bool:
        # Implement Slack API call
        print(f"Sending to Slack: {message}")
        return True
