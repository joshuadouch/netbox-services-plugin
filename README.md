## NetBox Services

Manage services such as web and mail hosts in NetBox

### Install / upgrade
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
### Screenshots

![image](https://github.com/user-attachments/assets/a65343f6-bd2b-4cea-9764-883dbf1739cf)
![image](https://github.com/user-attachments/assets/3c173da3-6328-4ea2-8319-456fc23ab352)
