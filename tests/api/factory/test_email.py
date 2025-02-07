from api.factory import EmailNotificationFactory


def test_email_notification():
    assert EmailNotificationFactory().send_notification(message="Hello World") is True
