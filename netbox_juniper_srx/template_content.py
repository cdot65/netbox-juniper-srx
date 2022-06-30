from extras.plugins import PluginTemplateExtension


class SecurityZones(PluginTemplateExtension):
    model = "dcim.interface"

    def right_page(self):
        return self.render(
            "netbox_juniper_srx/interface_zone.html",
            extra_context={
                "security_zones": self.context["object"].security_zones.all(),
            },
        )


template_extensions = [SecurityZones]
