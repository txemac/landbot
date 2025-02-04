from rest_framework import serializers


class HealthSerializer(serializers.Serializer):
    title = serializers.CharField()
    status = serializers.CharField()
    version = serializers.CharField()
    time = serializers.DateTimeField()
