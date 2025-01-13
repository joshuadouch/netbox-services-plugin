from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import WebServerSerializer, WebsiteSerializer, MailDomainSerializer, MailboxSerializer
from django.db.models import Count

class WebServerViewSet(NetBoxModelViewSet):
    queryset = models.WebServer.objects.prefetch_related('tags')
    serializer_class = WebServerSerializer

class WebsiteViewSet(NetBoxModelViewSet):
    queryset = models.Website.objects.prefetch_related(
        'tags'
    )
    serializer_class = WebsiteSerializer

class MailDomainViewSet(NetBoxModelViewSet):
    queryset = models.MailDomain.objects.prefetch_related('tags')
    serializer_class = MailDomainSerializer

class MailboxViewSet(NetBoxModelViewSet):
    queryset = models.Mailbox.objects.prefetch_related(
        'tags'
    )
    serializer_class = MailboxSerializer
