from api.factory import SlackNotificationFactory


def test_slack_notification():
    assert SlackNotificationFactory().send_notification(message="Hello World") is True
