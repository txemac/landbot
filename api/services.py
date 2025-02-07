from api.factory import CHANNELS
from api.messages import ERROR_UNSUPPORTED_TOPIC


def get_notification_service(
    topic: str,
):
    topic = topic.lower()
    if topic not in CHANNELS.keys():
        raise ValueError(ERROR_UNSUPPORTED_TOPIC)

    return CHANNELS[topic]
