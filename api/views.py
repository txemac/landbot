from datetime import UTC
from datetime import datetime

from api.messages import ERROR_VALIDATE_PARAMETERS
from api.messages import NOTIFICATION_SENT
from api.services import get_notification_service
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
        responses={
            status.HTTP_200_OK: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    title=openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description=API_TITLE,
                    ),
                    status=openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="OK",
                    ),
                    version=openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description=API_VERSION,
                    ),
                    time=openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description=str(datetime.now(UTC)),
                    ),
                ),
                required=["topic", "description"],
            ),
        },
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


class NotificationView(APIView):

    @swagger_auto_schema(
        operation_summary="Create a notification",
        operation_description="Receives a topic and description, then forwards the message to the appropriate channel "
        "(Slack or Email).",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties=dict(
                topic=openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Notification topic (e.g.: sales, pricing)",
                ),
                description=openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Description of the problem that needs assistance from.",
                ),
            ),
            required=["topic", "description"],
        ),
        responses={
            status.HTTP_200_OK: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    message=openapi.Schema(type=openapi.TYPE_STRING, description=f"{NOTIFICATION_SENT} by channel"),
                ),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    error=openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description=ERROR_VALIDATE_PARAMETERS,
                    ),
                ),
            ),
        },
    )
    def post(self, request):
        data = request.data
        topic = data.get("topic")
        description = data.get("description")

        if not topic or not description:
            return Response(data={"error": ERROR_VALIDATE_PARAMETERS}, status=status.HTTP_400_BAD_REQUEST)

        try:
            service = get_notification_service(topic=topic)
            service.send_notification(message=description)
            return Response(data={"message": f"{NOTIFICATION_SENT} by {service.NAME}"}, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response(data={"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
