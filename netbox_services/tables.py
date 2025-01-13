import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import WebServer, Website, MailDomain, Mailbox

class WebServerTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    site_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = WebServer
        fields = ('pk', 'id', 'name', 'host_server', 'site_count', 'comments', 'actions')
        default_columns = ('name', 'host_server', 'site_count')

class WebsiteTable(NetBoxTable):
    web_server = tables.Column(
        linkify=True
    )
    domain = tables.Column(
        linkify=True
    )
    type = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = Website
        fields = (
            'pk', 'id', 'web_server', 'domain', 'type', 'description', 'actions',
        )
        default_columns = (
            'domain', 'web_server', 'type', 'actions',
        )

class MailDomainTable(NetBoxTable):
    mail_domain = tables.Column(
        linkify=True
    )

    mailbox_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = MailDomain
        fields = ('pk', 'id', 'mail_domain', 'mailbox_count', 'comments', 'actions')
        default_columns = ('mail_domain', 'mailbox_count')

class MailboxTable(NetBoxTable):
    mail_domain = tables.Column(
        linkify=True
    )
    local_part = tables.Column(
        linkify=True
    )
    fqda = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = Mailbox
        fields = (
            'pk', 'id', 'fqda', 'local_part', 'mail_domain', 'description', 'actions',
        )
        default_columns = (
            'fqda', 'mail_domain', 'actions',
        )

class SimpleMailboxTable(NetBoxTable):
    mail_domain = tables.Column(
        linkify=True
    )   
    local_part = tables.Column(
        linkify=True
    )    
    
    class Meta(NetBoxTable.Meta):
        model = Mailbox
        fields = (
            'pk', 'id', 'local_part', 'mail_domain', 'description', 'actions',
        )   
        default_columns = (
            'local_part', 'mail_domain', 'actions',
        )
