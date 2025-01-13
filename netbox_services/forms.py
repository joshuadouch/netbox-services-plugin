from django import forms
from django.utils.translation import gettext_lazy as _
from virtualization.models import VirtualMachine
from utilities.forms.fields import CommentField, DynamicModelChoiceField, CSVModelChoiceField, CSVChoiceField
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm
from .models import WebServer, Website, MailDomain, Mailbox, TypeChoices

class WebServerForm(NetBoxModelForm):
    host_server = DynamicModelChoiceField(
        queryset=VirtualMachine.objects.all()
    )
    comments = CommentField()

    class Meta:
        model = WebServer
        fields = ('name', 'host_server', 'comments', 'tags')

class WebServerImportForm(NetBoxModelImportForm):

    name = forms.CharField(
        required=True,
        label=_("Name"),
    )   
    
    host_server = CSVModelChoiceField(
        queryset=VirtualMachine.objects.all(),
        to_field_name="name",
        required=True,
        label=_("Host server virtual machine name"),
        error_messages={
            "invalid_choice": _("Virtual machine %(value)s not found"),
        },  
    )   
    
    class Meta:
        model = WebServer
        fields = (
            'name', 'host_server', 'comments', 'tags',
        )

class WebsiteForm(NetBoxModelForm):
    web_server = DynamicModelChoiceField(
        queryset=WebServer.objects.all()
    )

    class Meta:
        model = Website
        fields = (
            'web_server', 'domain', 'type', 'description', 'tags',
        )

class WebsiteImportForm(NetBoxModelImportForm):
    
    web_server = CSVModelChoiceField(
        queryset=WebServer.objects.all(),
        to_field_name="name",
        required=True,
        label=_("Web server"),
        error_messages={
            "invalid_choice": _("Web server %(value)s not found"),
        },  
    )   
    
    domain = forms.CharField(
        required=True,
        label=_("Website domain"),
    )

    type = CSVChoiceField(
        choices=TypeChoices,
        required=True,
        label=_("Type"),
    )

    class Meta:
        model = Website
        fields = (
            'domain', 'web_server', 'type', 'description', 'tags',
        )

class MailDomainForm(NetBoxModelForm):

    comments = CommentField()

    class Meta:
        model = MailDomain
        fields = ('mail_domain', 'comments', 'tags')

class MailDomainImportForm(NetBoxModelImportForm):

    mail_domain = forms.CharField(
        required=True,
        label=_("Mail domain"),
    )
    
    class Meta:
        model = MailDomain
        fields = (
            'mail_domain', 'comments', 'tags',
        )

class MailboxForm(NetBoxModelForm):
    mail_domain = DynamicModelChoiceField(
        queryset=MailDomain.objects.all()
    )

    class Meta:
        model = Mailbox
        fields = (
            'local_part', 'mail_domain', 'description', 'tags',
        )

class MailboxImportForm(NetBoxModelImportForm):

    local_part = forms.CharField(
        required=True,
        label=_("Local part"),
    )

    mail_domain = CSVModelChoiceField(
        queryset=MailDomain.objects.all(),
        to_field_name="mail_domain",
        required=True,
        label=_("Mail domain"),
        error_messages={
            "invalid_choice": _("Mail Domain %(value)s not found"),
        },
    )

    class Meta:
        model = Mailbox
        fields = (
            'local_part', 'mail_domain', 'description', 'tags',
        )


