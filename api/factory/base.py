from abc import ABC
from abc import abstractmethod


class NotificationFactory(ABC):

    @abstractmethod
    def send_notification(
        self,
        message: str,
    ) -> bool:
        """
        Send notification.

        :param message: message
        :return: True if successful, False otherwise.
        """
        pass
