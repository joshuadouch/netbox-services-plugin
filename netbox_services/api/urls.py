from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_services'

router = NetBoxRouter()
router.register('web-servers', views.WebServerViewSet)
router.register('websites', views.WebsiteViewSet)
router.register('mail-domains', views.MailDomainViewSet)
router.register('mailboxes', views.MailboxViewSet)

urlpatterns = router.urls
