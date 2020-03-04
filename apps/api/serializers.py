from rest_framework.serializers import ModelSerializer

from apps.document.models import Document

__all__ = [
    'DocumentSerializer'
]


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
