from rest_framework import serializers
from .models import UserMessageInput


class ChatResponseSerializer(serializers.Serializer):
    tag = serializers.CharField(read_only=True)
    message = serializers.CharField(read_only=True)


class UserMessageInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessageInput
        fields = ('message', 'identified_tag', )
        extra_kwargs = {'identified_tag': {'required': False}}

    def save(self, identified_tag, **kwargs):
        data = {"identified_tag": identified_tag, **kwargs}
        return super().save(**data)
