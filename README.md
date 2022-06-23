# Juniper Security NetBox Plugin

This [Netbox](https://github.com/cdot65/netbox-juniper-security) plugin will enable you to document the various security components of a Juniper SRX firewall.

## Compatibility

`netbox-juniper-security` was built with NetBox version 3.2 in mind, please create an Issue if there are any compatibility issues with previous versions.

| Netbox | Plugin |
|---|---|
| 3.2 | 0.0.1 |

## Installation

After activating NetBox's virtual environment, follow the [standard Python package installation instructions](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-from-pypi) to install the `netbox-juniper-security` plugin.

```bash
$ source /opt/netbox/venv/bin/activate
$ pip install netbox-juniper-security
```

We will need to tell NetBox to look for our plugin within the `/opt/netbox/netbox/netbox/configuration.py` file

```python
PLUGINS = ['netbox_juniper_security']
```

Add `netbox-juniper-security` to your local_requirements.txt

```bash
$ echo 'netbox-juniper-security' >> /opt/netbox/local_requirements.txt
```

Restart NetBox with systemd

```bash
$ systemctl restart netbox.service
```

## Screenshots

Security Policy Rules
![Security Policy Rules](https://raw.githubusercontent.com/cdot65/netbox-juniper-security/main/site/content/assets/images/security_policy_rules.png)
