from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    # Web servers
    path('web-servers/', views.WebServerListView.as_view(), name='webserver_list'),
    path('web-servers/add/', views.WebServerEditView.as_view(), name='webserver_add'),
    path('web-servers/<int:pk>/', views.WebServerView.as_view(), name='webserver'),
    path('web-servers/<int:pk>/edit/', views.WebServerEditView.as_view(), name='webserver_edit'),
    path('web-servers/<int:pk>/delete/', views.WebServerDeleteView.as_view(), name='webserver_delete'),
    path('web-servers/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='webserver_changelog', kwargs={
        'model': models.WebServer
    }),

    # Web server sites
    path('websites/', views.WebsiteListView.as_view(), name='website_list'),
    path('websites/add/', views.WebsiteEditView.as_view(), name='website_add'),
    path('websites/<int:pk>/', views.WebsiteView.as_view(), name='website'),
    path('websites/<int:pk>/edit/', views.WebsiteEditView.as_view(), name='website_edit'),
    path('websites/<int:pk>/delete/', views.WebsiteDeleteView.as_view(), name='website_delete'),
    path('websites/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='website_changelog', kwargs={
        'model': models.Website
    }),

    # Mail domains
    path('mail-domains/', views.MailDomainListView.as_view(), name='maildomain_list'),
    path('mail-domains/add/', views.MailDomainEditView.as_view(), name='maildomain_add'),
    path('mail-domains/<int:pk>/', views.MailDomainView.as_view(), name='maildomain'),
    path('mail-domains/<int:pk>/edit/', views.MailDomainEditView.as_view(), name='maildomain_edit'),
    path('mail-domains/<int:pk>/delete/', views.MailDomainDeleteView.as_view(), name='maildomain_delete'),
    path('mail-domains/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='maildomain_changelog', kwargs={
        'model': models.MailDomain
    }),

    # Mailboxes
    path('mailboxes/', views.MailboxListView.as_view(), name='mailbox_list'),
    path('mailboxes/add/', views.MailboxEditView.as_view(), name='mailbox_add'),
    path('mailboxes/<int:pk>/', views.MailboxView.as_view(), name='mailbox'),
    path('mailboxes/<int:pk>/edit/', views.MailboxEditView.as_view(), name='mailbox_edit'),
    path('mailboxes/<int:pk>/delete/', views.MailboxDeleteView.as_view(), name='mailbox_delete'),
    path('mailboxes/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='mailbox_changelog', kwargs={
        'model': models.Mailbox
    }),
)
