## Netbox Services plugin

Manage services such as web and mail hosts in Netbox

### Installation
```
$ cd /opt/netbox && source /opt/netbox/venv/bin/activate
(venv) $ sudo /opt/netbox/venv/bin/python -m pip install git+https://github.com/joshuadouch/netbox-services-plugin
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
Run migrations
```
cd /opt/netbox && python netbox/manage.py migrate
```
Restart Netbox
```
sudo systemctl restart netbox netbox-rq
```
