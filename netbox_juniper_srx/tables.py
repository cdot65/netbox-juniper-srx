import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import SecurityPolicy, SecurityPolicyRule, SecurityZone


class SecurityPolicyTable(NetBoxTable):
    name = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    default_action = ChoiceFieldColumn()
    rule_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = SecurityPolicy
        fields = (
            "pk",
            "id",
            "device",
            "site",
            "tenant",
            "name",
            "from_zone",
            "to_zone",
            "default_action",
            "description",
            "comments",
            "actions",
        )
        default_columns = (
            "device",
            "name",
            "from_zone",
            "to_zone",
            "default_action",
            "description",
        )


class SecurityPolicyRuleTable(NetBoxTable):
    device = tables.Column(linkify=True)
    security_policy = tables.Column(linkify=True)
    index = tables.Column(linkify=True)
    action = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = SecurityPolicyRule
        fields = (
            "pk",
            "id",
            "action",
            "address_source",
            "address_destination",
            "application",
            "dynamic_application",
            "description",
            "index",
            "name",
            "security_policy",
        )
        default_columns = (
            "index",
            "security_policy",
            "name",
            "description",
            "address_source",
            "address_destination",
            "application",
            "action",
            "actions",
        )


class SecurityZoneTable(NetBoxTable):
    name = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    match_interfaces = tables.Column(linkify=True)
    inbound_protocols = tables.Column()
    inbound_services = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = SecurityZone
        fields = (
            "pk",
            "id",
            "device",
            "site",
            "tenant",
            "name",
            "match_interfaces",
            "inbound_protocols",
            "inbound_services",
            "description",
            "comments",
            "actions",
        )
        default_columns = (
            "device",
            "name",
            "match_interfaces",
            "inbound_protocols",
            "inbound_services",
            "description",
        )
