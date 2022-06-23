from extras.plugins import PluginConfig


class NetBoxJuniperSecurityConfig(PluginConfig):
    name = "netbox_juniper_security"
    verbose_name = "Netbox Juniper Security Plugin"
    description = "Manage your Juniper SRX firewall security configuration in Netbox."
    version = "0.1"
    base_url = "juniper_security"


config = NetBoxJuniperSecurityConfig
