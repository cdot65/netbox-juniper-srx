from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField
from .models import SecurityPolicy, SecurityPolicyRule, SecurityZone
from dcim.models import Interface


class SecurityPolicyForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = SecurityPolicy
        fields = (
            "name",
            "device",
            "from_zone",
            "to_zone",
            "default_action",
            "description",
            "comments",
            "tags",
        )


class SecurityPolicyRuleForm(NetBoxModelForm):
    security_policy = DynamicModelChoiceField(queryset=SecurityPolicy.objects.all())

    class Meta:
        model = SecurityPolicyRule
        fields = (
            "address_source",
            "address_destination",
            "application",
            "dynamic_application",
            "description",
            "index",
            "name",
            "security_policy",
            "device",
            "action",
            "tags",
        )


class SecurityPolicyRuleFilterForm(NetBoxModelFilterSetForm):
    model = SecurityPolicyRule
    security_policy = forms.ModelMultipleChoiceField(
        queryset=SecurityPolicy.objects.all(), required=False
    )
    index = forms.IntegerField(required=False)


class SecurityZoneForm(NetBoxModelForm):
    match_interfaces = DynamicModelChoiceField(queryset=Interface.objects.all())
    comments = CommentField()

    class Meta:
        model = SecurityZone
        fields = (
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
        )
