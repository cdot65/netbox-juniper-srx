from netbox.filtersets import NetBoxModelFilterSet
from .models import SecurityPolicyRule


class SecurityPolicyRuleFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = SecurityPolicyRule
        fields = (
            "id",
            "security_policy",
            "index",
            "address_source",
            "address_destination",
            "application",
            "name",
            "action",
        )

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
