from extras.plugins import PluginConfig


class NetBoxJuniperSrxConfig(PluginConfig):
    name = "netbox_juniper_srx"
    verbose_name = "Netbox Juniper SRX Plugin"
    description = "Manage your Juniper SRX firewall security configuration in Netbox."
    version = "0.0.2"
    base_url = "juniper-srx"


config = NetBoxJuniperSrxConfig
