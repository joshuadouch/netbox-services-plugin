from django.utils.translation import gettext_lazy as _

from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from netbox.plugins.utils import get_plugin_config

menu_name = "Services"

webserver_menu_item = PluginMenuItem(
    link="plugins:netbox_services:webserver_list",
    link_text=_("Web Servers"),
    buttons=(
        PluginMenuButton(
            "plugins:netbox_services:webserver_add",
            _("Add"),
            "mdi mdi-plus-thick",
        ),
        PluginMenuButton(
            "plugins:netbox_services:webserver_bulk_import",
            _("Import"),
            "mdi mdi-upload",
        ),
    ),
)

website_menu_item = PluginMenuItem(
    link="plugins:netbox_services:website_list",
    link_text=_("Websites"),
    buttons=(
        PluginMenuButton(
            "plugins:netbox_services:website_add",
            _("Add"),
            "mdi mdi-plus-thick",
        ),
        PluginMenuButton(
            "plugins:netbox_services:website_bulk_import",
            _("Import"),
            "mdi mdi-upload",
        ),
    ),
)

maildomain_menu_item = PluginMenuItem(
    link="plugins:netbox_services:maildomain_list",
    link_text=_("Domains"),
    buttons=(
        PluginMenuButton(
            "plugins:netbox_services:maildomain_add",
            _("Add"),
            "mdi mdi-plus-thick",
        ),
        PluginMenuButton(
            "plugins:netbox_services:maildomain_bulk_import",
            _("Import"),
            "mdi mdi-upload",
        ),
    ),
)

mailbox_menu_item = PluginMenuItem(
    link="plugins:netbox_services:mailbox_list",
    link_text=_("Mailboxes"),
    buttons=(
        PluginMenuButton(
            "plugins:netbox_services:mailbox_add",
            _("Add"),
            "mdi mdi-plus-thick",
        ),
        PluginMenuButton(
            "plugins:netbox_services:mailbox_bulk_import",
            _("Import"),
            "mdi mdi-upload",
        ),
    ),
)

menu = PluginMenu(
    label=menu_name,
    groups=(
        (
            _("Web"),
            (
                webserver_menu_item,
                website_menu_item,
            ),
        ),
        (
            _("Mail"),
            (
                maildomain_menu_item,
                mailbox_menu_item,
            ),
        ),
    ),
    icon_class="mdi mdi-web",
)

