from django.contrib.postgres.fields import ArrayField
from django.db import models
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.urls import reverse

class TypeChoices(ChoiceSet):
    key = 'Website.domain'

    CHOICES = [
        ('wordpress', 'WordPress'),
        ('reverse-proxy', 'Reverse Proxy'),
        ('other', 'Other'),
    ]

class WebServer(NetBoxModel):
    name = models.CharField(
        max_length=100
    )
    host_server = models.ForeignKey(
        to='virtualization.VirtualMachine',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_services:webserver', args=[self.pk])


class Website(NetBoxModel):
    web_server = models.ForeignKey(
        to=WebServer,
        on_delete=models.CASCADE,
        related_name='websites'
    )
    domain = models.CharField(
        max_length=100
    )
    type = models.CharField(
        max_length=30,
        choices=TypeChoices
    )
    description = models.CharField(
        max_length=500,
        blank=True
    )
    class Meta:
        ordering = ('web_server', 'domain')
        unique_together = ('web_server', 'domain')

    def __str__(self):
        return self.domain

    def get_absolute_url(self):
        return reverse('plugins:netbox_services:website', args=[self.pk])

class MailDomain(NetBoxModel):
    mail_domain = models.CharField(
        max_length=500
    )

    comments = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ('mail_domain',)

    def __str__(self):
        return self.mail_domain

    def get_absolute_url(self):
        return reverse('plugins:netbox_services:maildomain', args=[self.pk])

class Mailbox(NetBoxModel):

    local_part = models.CharField(
        max_length=100
    )   

    mail_domain = models.ForeignKey(
        to=MailDomain,
        on_delete=models.CASCADE,
        related_name='mailboxes'
    )

    description = models.CharField(
        max_length=500,
        blank=True
    )   
    class Meta:
        ordering = ('local_part', 'mail_domain')
        unique_together = ('local_part', 'mail_domain')
        verbose_name_plural = "mailboxes"
        
    def __str__(self):
        return str(self.local_part) + "@" + str(self.mail_domain)
        
    def get_absolute_url(self):
        return reverse('plugins:netbox_services:mailbox', args=[self.pk])
