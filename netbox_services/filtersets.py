from netbox.filtersets import NetBoxModelFilterSet
from .models import WebServer, Website, MailDomain, Mailbox

class WebServerFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = WebServer
        fields = ('name', 'host_server')
        
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

class WebsiteFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Website
        fields = ('domain', 'web_server', 'type')
        
    def search(self, queryset, name, value):
        return queryset.filter(domain__icontains=value)

class MailDomainFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = MailDomain
        fields = ('mail_domain',)
        
    def search(self, queryset, name, value):
        return queryset.filter(mail_domain__icontains=value)

class MailboxFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Mailbox
        fields = ('local_part', 'mail_domain')
        
    def search(self, queryset, name, value):
        return queryset.filter(mail_domain__icontains=value)