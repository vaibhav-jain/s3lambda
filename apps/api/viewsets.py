from rest_framework.viewsets import ModelViewSet

from apps.document.models import Document
from .serializers import DocumentSerializer

__all__ = [
    'DocumentViewSet'
]


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
