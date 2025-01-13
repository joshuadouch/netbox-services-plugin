from netbox.views import generic
from django.db.models import CharField, Value, Count
from django.db.models.functions import Concat
from netbox_services.models import WebServer, Website, MailDomain, Mailbox
from netbox_services.tables import WebServerTable, WebsiteTable, MailDomainTable, MailboxTable, SimpleMailboxTable
from netbox_services.forms import WebServerForm, WebsiteForm, MailDomainForm, MailboxForm, WebServerImportForm, WebsiteImportForm, MailDomainImportForm, MailboxImportForm

class WebServerView(generic.ObjectView):
    queryset = WebServer.objects.all()
    def get_extra_context(self, request, instance):
        table = WebsiteTable(instance.websites.all())
        table.configure(request)

        return {
            'sites_table': table,
        }

class WebServerListView(generic.ObjectListView):
    queryset = WebServer.objects.annotate(
        site_count=Count('websites')
    )
    table = WebServerTable

class WebServerEditView(generic.ObjectEditView):
    queryset = WebServer.objects.all()
    form = WebServerForm

class WebServerDeleteView(generic.ObjectDeleteView):
    queryset = WebServer.objects.all()

class WebServerBulkImportView(generic.BulkImportView):
    queryset = WebServer.objects.all()
    model_form = WebServerImportForm
    table = WebServerTable
    default_return_url = "plugins:netbox_services:webserver_list"

class WebsiteView(generic.ObjectView):
    queryset = Website.objects.all()

class WebsiteListView(generic.ObjectListView):
    queryset = Website.objects.all()
    table = WebsiteTable

class WebsiteEditView(generic.ObjectEditView):
    queryset = Website.objects.all()
    form = WebsiteForm

class WebsiteDeleteView(generic.ObjectDeleteView):
    queryset = Website.objects.all()

class WebsiteBulkImportView(generic.BulkImportView):
    queryset = Website.objects.all()
    model_form = WebsiteImportForm
    table = WebsiteTable
    default_return_url = "plugins:netbox_services:website_list"

class MailDomainView(generic.ObjectView):
    queryset = MailDomain.objects.all()
    def get_extra_context(self, request, instance):
        table = SimpleMailboxTable(instance.mailboxes.all())
        table.configure(request)

        return {
            'mailboxes_table': table,
        }

class MailDomainListView(generic.ObjectListView):
    queryset = MailDomain.objects.annotate(
        mailbox_count=Count('mailboxes')
    )
    table = MailDomainTable

class MailDomainEditView(generic.ObjectEditView):
    queryset = MailDomain.objects.all()
    form = MailDomainForm

class MailDomainDeleteView(generic.ObjectDeleteView):
    queryset = MailDomain.objects.all()

class MailDomainBulkImportView(generic.BulkImportView):
    queryset = MailDomain.objects.all()
    model_form = MailDomainImportForm
    table = MailDomainTable
    default_return_url = "plugins:netbox_services:maildomain_list"

class MailboxView(generic.ObjectView):
    queryset = Mailbox.objects.all()

class MailboxListView(generic.ObjectListView):
    queryset = Mailbox.objects.annotate(
        fqda=Concat('local_part', Value('@'), 'mail_domain__mail_domain', output_field=CharField())
    )
    table = MailboxTable

class MailboxEditView(generic.ObjectEditView):
    queryset = Mailbox.objects.all()
    form = MailboxForm

class MailboxDeleteView(generic.ObjectDeleteView):
    queryset = Mailbox.objects.all()

class MailboxBulkImportView(generic.BulkImportView):
    queryset = Mailbox.objects.all()
    model_form = MailboxImportForm
    table = MailboxTable
    default_return_url = "plugins:netbox_services:mailbox_list"
