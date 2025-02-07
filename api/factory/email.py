from api.factory.base import NotificationFactory


class EmailNotificationFactory(NotificationFactory):

    NAME = "Email"

    def send_notification(
        self,
        message: str,
    ) -> bool:
        # Mock email sending
        print(f"Sending Email: {message}")
        return True
