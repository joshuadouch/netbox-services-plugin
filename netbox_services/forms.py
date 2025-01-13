from virtualization.models import VirtualMachine
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from netbox.forms import NetBoxModelForm
from .models import WebServer, Website, MailDomain, Mailbox

class WebServerForm(NetBoxModelForm):
    host_server = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all()
    )
    comments = CommentField()

    class Meta:
        model = WebServer
        fields = ('name', 'host_server', 'comments', 'tags')

class WebsiteForm(NetBoxModelForm):
    web_server = DynamicModelChoiceField(
        queryset=WebServer.objects.all()
    )

    class Meta:
        model = Website
        fields = (
            'web_server', 'domain', 'type', 'description', 'tags',
        )

class MailDomainForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = MailDomain
        fields = ('mail_domain', 'comments', 'tags')

class MailboxForm(NetBoxModelForm):
    mail_domain = DynamicModelChoiceField(
        queryset=MailDomain.objects.all()
    )

    class Meta:
        model = Mailbox
        fields = (
            'local_part', 'mail_domain', 'description', 'tags',
        )
