from netbox.views import generic
from . import forms, models, tables
from django.db.models import CharField, Value, Count
from django.db.models.functions import Concat

class WebServerView(generic.ObjectView):
    queryset = models.WebServer.objects.all()
    def get_extra_context(self, request, instance):
        table = tables.WebsiteTable(instance.websites.all())
        table.configure(request)

        return {
            'sites_table': table,
        }

class WebServerListView(generic.ObjectListView):
    queryset = models.WebServer.objects.annotate(
        site_count=Count('websites')
    )
    table = tables.WebServerTable

class MailDomainView(generic.ObjectView):
    queryset = models.MailDomain.objects.all()
    def get_extra_context(self, request, instance):
        table = tables.SimpleMailboxTable(instance.mailboxes.all())
        table.configure(request)

        return {
            'mailboxes_table': table,
        }

class MailDomainListView(generic.ObjectListView):
    queryset = models.MailDomain.objects.annotate(
        mailbox_count=Count('mailboxes')
    )
    table = tables.MailDomainTable

class WebServerEditView(generic.ObjectEditView):
    queryset = models.WebServer.objects.all()
    form = forms.WebServerForm

class WebServerDeleteView(generic.ObjectDeleteView):
    queryset = models.WebServer.objects.all()

class MailDomainEditView(generic.ObjectEditView):
    queryset = models.MailDomain.objects.all()
    form = forms.MailDomainForm

class MailDomainDeleteView(generic.ObjectDeleteView):
    queryset = models.MailDomain.objects.all()

class WebsiteView(generic.ObjectView):
    queryset = models.Website.objects.all()

class WebsiteListView(generic.ObjectListView):
    queryset = models.Website.objects.all()
    table = tables.WebsiteTable

class WebsiteEditView(generic.ObjectEditView):
    queryset = models.Website.objects.all()
    form = forms.WebsiteForm

class WebsiteDeleteView(generic.ObjectDeleteView):
    queryset = models.Website.objects.all()

class MailboxView(generic.ObjectView):
    queryset = models.Mailbox.objects.all()

class MailboxListView(generic.ObjectListView):
    queryset = models.Mailbox.objects.annotate(
        fqda=Concat('local_part', Value('@'), 'mail_domain__mail_domain', output_field=CharField())
    )
    table = tables.MailboxTable

class MailboxEditView(generic.ObjectEditView):
    queryset = models.Mailbox.objects.all()
    form = forms.MailboxForm

class MailboxDeleteView(generic.ObjectDeleteView):
    queryset = models.Mailbox.objects.all()
