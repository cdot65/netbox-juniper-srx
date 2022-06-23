from django.db.models import Count
from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import SecurityPolicySerializer, SecurityPolicyRuleSerializer


class SecurityPolicyViewSet(NetBoxModelViewSet):
    queryset = models.SecurityPolicy.objects.prefetch_related("tags").annotate(
        rule_count=Count("rules")
    )
    serializer_class = SecurityPolicySerializer


class SecurityPolicyRuleViewSet(NetBoxModelViewSet):
    queryset = models.SecurityPolicyRule.objects.prefetch_related(
        "security_policy", "tags"
    )
    serializer_class = SecurityPolicyRuleSerializer
    filterset_class = filtersets.SecurityPolicyRuleFilterSet
