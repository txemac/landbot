from datetime import UTC
from datetime import datetime

from landbot.settings import API_TITLE
from landbot.settings import API_VERSION
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthView(APIView):
    def get(
        self,
        request,
    ) -> Response:
        response_data = dict(
            title=API_TITLE,
            status="OK",
            version=API_VERSION,
            time=datetime.now(UTC),
        )
        return Response(response_data, status=status.HTTP_200_OK)
