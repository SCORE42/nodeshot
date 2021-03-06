from rest_framework import serializers

from .models import Inward


__all__ = [
    'InwardSerializer',
]


class InwardSerializer(serializers.ModelSerializer):
    """ status icons """

    class Meta:
        model = Inward
        read_only_fields = (
            'status', 'added', 'updated', 'content_type', 'object_id',
            'user', 'ip', 'user_agent', 'accept_language')
        fields = '__all__'
