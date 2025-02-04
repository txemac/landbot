from datetime import UTC
from datetime import datetime

from api.serializer import HealthSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from landbot.settings import API_TITLE
from landbot.settings import API_VERSION
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthView(APIView):

    @swagger_auto_schema(
        tags=["Health"],
        operation_summary="Health check",
        operation_description="Checks the health status of the system.",
        responses={status.HTTP_200_OK: openapi.Response(description="Health status OK", schema=HealthSerializer)},
    )
    def get(
        self,
        request,
    ) -> Response:
        return Response(
            dict(
                title=API_TITLE,
                status="OK",
                version=API_VERSION,
                time=datetime.now(UTC),
            ),
            status=status.HTTP_200_OK,
        )
