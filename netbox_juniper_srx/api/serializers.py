from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import SecurityPolicy, SecurityPolicyRule, SecurityZone


class NestedSecurityPolicySerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_juniper_srx-api:securitypolicy-detail"
    )

    class Meta:
        model = SecurityPolicy
        fields = ("id", "url", "display", "name")


class NestedSecurityPolicyRuleSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_juniper_srx-api:securitypolicyrule-detail"
    )

    class Meta:
        model = SecurityPolicyRule
        fields = ("id", "url", "display", "index")


class SecurityPolicySerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_juniper_srx-api:securitypolicy-detail"
    )
    rule_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = SecurityPolicy
        fields = (
            "id",
            "url",
            "display",
            "name",
            "from_zone",
            "to_zone",
            "default_action",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
            "rule_count",
        )


class SecurityPolicyRuleSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_juniper_srx-api:securitypolicyrule-detail"
    )
    security_policy = NestedSecurityPolicySerializer()

    class Meta:
        model = SecurityPolicyRule
        fields = (
            "id",
            "url",
            "display",
            "security_policy",
            "name",
            "address_source",
            "address_destination",
            "application",
            "dynamic_application",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
            "description",
        )


class SecurityZoneSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:netbox_juniper_srx-api:securityzone-detail"
    )

    class Meta:
        model = SecurityZone
        fields = (
            "id",
            "url",
            "display",
            "name",
            "device",
            "match_interfaces",
            "inbound_protocols",
            "inbound_services",
            "app_tracking",
            "status",
            "description",
            "comments",
            "tags",
            "custom_fields",
            "created",
            "last_updated",
        )
