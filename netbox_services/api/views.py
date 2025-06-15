from netbox.api.viewsets import NetBoxModelViewSet
from .. import filtersets, models
from .serializers import WebServerSerializer, WebsiteSerializer, MailDomainSerializer, MailboxSerializer
from django.db.models import Count

class WebServerViewSet(NetBoxModelViewSet):
    queryset = models.WebServer.objects.prefetch_related('tags')
    serializer_class = WebServerSerializer
    filterset_class = filtersets.WebServerFilterSet

class WebsiteViewSet(NetBoxModelViewSet):
    queryset = models.Website.objects.prefetch_related(
        'tags'
    )
    serializer_class = WebsiteSerializer
    filterset_class = filtersets.WebsiteFilterSet

class MailDomainViewSet(NetBoxModelViewSet):
    queryset = models.MailDomain.objects.prefetch_related('tags')
    serializer_class = MailDomainSerializer
    filterset_class = filtersets.MailDomainFilterSet

class MailboxViewSet(NetBoxModelViewSet):
    queryset = models.Mailbox.objects.prefetch_related(
        'tags'
    )
    serializer_class = MailboxSerializer
    filterset_class = filtersets.MailboxFilterSet