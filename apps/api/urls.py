from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from apps.api.viewsets import DocumentViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'documents', DocumentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url('', include(router.urls)),
]
