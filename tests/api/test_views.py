from api.messages import ERROR_VALIDATE_PARAMETERS
from api.messages import NOTIFICATION_SENT
from django.test import SimpleTestCase
from django.urls import reverse
from landbot.settings import API_TITLE
from landbot.settings import API_VERSION
from rest_framework import status
from rest_framework.test import APIClient
from tests.utils import assert_dicts


class HealthTests(SimpleTestCase):

    def setUp(self):
        self.client = APIClient()

    def test_health_200(self):
        url = reverse("health")

        response = self.client.get(url)

        assert response.status_code == status.HTTP_200_OK
        expected = dict(
            title=API_TITLE,
            status="OK",
            version=API_VERSION,
            time="*",
        )
        assert_dicts(original=response.json(), expected=expected)


class NotificationTests(SimpleTestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse("notify")
        self.data = dict(
            topic="Pricing",
            description="Help me please!",
        )

    def test_notification_no_topic(self):
        self.data.pop("topic")
        response = self.client.post(
            path=self.url,
            data=self.data,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["error"] == ERROR_VALIDATE_PARAMETERS

    def test_notification_no_description(self):
        self.data.pop("description")
        response = self.client.post(
            path=self.url,
            data=self.data,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json()["error"] == ERROR_VALIDATE_PARAMETERS

    def test_notification_email(self):
        self.data["topic"] = "Sales"
        response = self.client.post(
            path=self.url,
            data=self.data,
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["message"] == f"{NOTIFICATION_SENT} by Slack"

    def test_notification_slack(self):
        response = self.client.post(
            path=self.url,
            data=self.data,
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["message"] == f"{NOTIFICATION_SENT} by Email"

    def test_notification_invalid_topic(self):
        self.data["topic"] = "invalid"
        response = self.client.post(
            path=self.url,
            data=self.data,
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
