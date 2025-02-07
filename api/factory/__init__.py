"""
Declare new channels and new topics here
"""

from api.factory.email import EmailNotificationFactory
from api.factory.slack import SlackNotificationFactory

CHANNELS = dict(
    sales=SlackNotificationFactory(),
    pricing=EmailNotificationFactory(),
)
