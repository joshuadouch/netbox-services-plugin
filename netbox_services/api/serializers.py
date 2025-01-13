from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import WebServer, Website, MailDomain, Mailbox

class WebServerSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_services-api:webserver-detail'
    )

    site_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = WebServer
        fields = (
            'id', 'url', 'display', 'name', 'host_server', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated', 'site_count',
        )

class WebsiteSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_services-api:website-detail'
    )

    class Meta:
        model = Website
        fields = (
            'id', 'url', 'display', 'web_server', 'domain', 'type', 'tags', 'custom_fields', 'created',
            'last_updated',
        )

class NestedMailDomainSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_services-api:maildomain-detail'
    )

    class Meta:
        model = MailDomain
        fields = ('id', 'url', 'display', 'mail_domain')

class NestedMailboxSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_services-api:mailbox-detail'
    )

    class Meta:
        model = Mailbox
        fields = ('id', 'url', 'display', 'local_part')

class MailDomainSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_services-api:maildomain-detail'
    )

    mailbox_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = MailDomain
        fields = (
            'id', 'url', 'display', 'mail_domain', 'comments', 'tags', 'custom_fields', 'created',
            'last_updated', 'mailbox_count',
        )

class MailboxSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_services-api:mailbox-detail'
    )
    mail_domain = NestedMailDomainSerializer()

    class Meta:
        model = Mailbox
        fields = (
            'id', 'url', 'display', 'local_part', 'mail_domain', 'tags', 'custom_fields', 'created',
            'last_updated',
        )
