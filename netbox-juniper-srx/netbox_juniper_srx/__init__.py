from extras.plugins import PluginConfig


class NetBoxJuniperSecurityConfig(PluginConfig):
    name = "netbox_juniper_srx"
    verbose_name = "Netbox Juniper SRX Plugin"
    description = "Manage your Juniper SRX firewall security configuration in Netbox."
    version = "0.1"
    base_url = "srx"


config = NetBoxJuniperSecurityConfig
