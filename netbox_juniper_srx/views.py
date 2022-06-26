from django.db.models import Count
from netbox.views import generic
from . import filtersets, forms, models, tables


class SecurityPolicyView(generic.ObjectView):
    queryset = models.SecurityPolicy.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.SecurityPolicyRuleTable(instance.rules.all())
        table.configure(request)

        return {
            "rules_table": table,
        }


class SecurityPolicyListView(generic.ObjectListView):
    queryset = models.SecurityPolicy.objects.annotate(rule_count=Count("rules"))
    table = tables.SecurityPolicyTable


class SecurityPolicyEditView(generic.ObjectEditView):
    queryset = models.SecurityPolicy.objects.all()
    form = forms.SecurityPolicyForm


class SecurityPolicyDeleteView(generic.ObjectDeleteView):
    queryset = models.SecurityPolicy.objects.all()


class SecurityPolicyRuleView(generic.ObjectView):
    queryset = models.SecurityPolicyRule.objects.all()


class SecurityPolicyRuleListView(generic.ObjectListView):
    queryset = models.SecurityPolicyRule.objects.all()
    table = tables.SecurityPolicyRuleTable
    filterset = filtersets.SecurityPolicyRuleFilterSet
    filterset_form = forms.SecurityPolicyRuleFilterForm


class SecurityPolicyRuleEditView(generic.ObjectEditView):
    queryset = models.SecurityPolicyRule.objects.all()
    form = forms.SecurityPolicyRuleForm


class SecurityPolicyRuleDeleteView(generic.ObjectDeleteView):
    queryset = models.SecurityPolicyRule.objects.all()


class SecurityZoneView(generic.ObjectView):
    queryset = models.SecurityZone.objects.all()

    # def get_extra_context(self, request, instance):
    #     table = tables.SecurityZoneInterfacesTable(instance.rules.all())
    #     table.configure(request)

    #     return {
    #         "interfaces_table": table,
    #     }


class SecurityZoneListView(generic.ObjectListView):
    queryset = models.SecurityZone.objects.all()
    table = tables.SecurityZoneTable


class SecurityZoneEditView(generic.ObjectEditView):
    queryset = models.SecurityZone.objects.all()
    form = forms.SecurityZoneForm


class SecurityZoneDeleteView(generic.ObjectDeleteView):
    queryset = models.SecurityZone.objects.all()
