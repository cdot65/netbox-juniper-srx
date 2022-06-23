from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


securitypolicy_buttons = [
    PluginMenuButton(
        link="plugins:netbox_juniper_srx:securitypolicy_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
    )
]

securitypolicyrule_buttons = [
    PluginMenuButton(
        link="plugins:netbox_juniper_srx:securitypolicyrule_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
    )
]

menu_items = (
    PluginMenuItem(
        link="plugins:netbox_juniper_srx:securitypolicy_list",
        link_text="Security Policies",
        buttons=securitypolicy_buttons,
    ),
    PluginMenuItem(
        link="plugins:netbox_juniper_srx:securitypolicyrule_list",
        link_text="Security Policy Rules",
        buttons=securitypolicyrule_buttons,
    ),
)
