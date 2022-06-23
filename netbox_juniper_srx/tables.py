import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import SecurityPolicy, SecurityPolicyRule


class SecurityPolicyTable(NetBoxTable):
    name = tables.Column(linkify=True)
    default_action = ChoiceFieldColumn()
    rule_count = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = SecurityPolicy
        fields = (
            "pk",
            "id",
            "name",
            "from_zone",
            "to_zone",
            "default_action",
            "comments",
            "actions",
        )
        default_columns = ("name", "from_zone", "to_zone", "default_action")


class SecurityPolicyRuleTable(NetBoxTable):
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
