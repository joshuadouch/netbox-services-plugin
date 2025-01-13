## Netbox Services plugin

Manage services such as web and mail hosts in Netbox

### Installation
Clone and install plugin
```
$ git clone https://github.com/joshuadouch/netbox-services-plugin.git
$ cd /opt/netbox && source /opt/netbox/venv/bin/activate
(venv) $ sudo /opt/netbox/venv/bin/pip install -e /path/to/netbox-services-plugin/
```
Add plugin to configuration
```
$ vim /opt/netbox/netbox/netbox/configuration.py

...
PLUGINS=[
"netbox_services",
]
...
```
