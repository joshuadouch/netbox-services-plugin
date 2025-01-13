from netbox.plugins import PluginConfig

class NetBoxServicesConfig(PluginConfig):
    name = 'netbox_services'
    verbose_name = ' NetBox Services'
    description = 'Manage services such as web and mail hosts in NetBox'
    version = '0.1'
    base_url = 'services'

config = NetBoxServicesConfig
