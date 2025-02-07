import pytest
from api.factory import EmailNotificationFactory
from api.factory import SlackNotificationFactory
from api.messages import ERROR_UNSUPPORTED_TOPIC

from api.services import get_notification_service


def test_get_services_slack():
    service = get_notification_service("Sales")

    assert isinstance(service, SlackNotificationFactory)


def test_get_services_email():
    service = get_notification_service("pricing")

    assert isinstance(service, EmailNotificationFactory)


def test_get_services_invalid():
    with pytest.raises(ValueError) as e:
        get_notification_service("invalid")

    assert ERROR_UNSUPPORTED_TOPIC in str(e.value)
