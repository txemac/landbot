from django.urls import reverse
from landbot.settings import API_TITLE
from landbot.settings import API_VERSION
from rest_framework import status
from tests.utils import assert_dicts


def test_health_200(client):
    url = reverse('health_check')

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    expected = dict(
        title=API_TITLE,
        status="OK",
        version=API_VERSION,
        time="*",
    )
    assert_dicts(original=response.json(), expected=expected)
