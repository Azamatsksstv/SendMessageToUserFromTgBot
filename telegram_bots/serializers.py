from rest_framework import serializers


class TelegramTokenSerializer(serializers.Serializer):
    chat_id = serializers.CharField()
    token = serializers.CharField()
