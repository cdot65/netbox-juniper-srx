from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


class SecurityZonesChoices(ChoiceSet):

    CHOICES = (
        ("home", "Home", "green"),
        ("lab", "Lab", "orange"),
        ("internet", "Internet", "cyan"),
        ("dmz", "DMZ", "red"),
    )


class PolicyActionChoices(ChoiceSet):

    DEFAULT = "permit"

    CHOICES = (
        ("permit", "Permit", "green"),
        ("log", "Log", "cyan"),
        ("deny", "Deny", "orange"),
        ("reject", "Reject", "red"),
    )


class RuleActionChoices(ChoiceSet):

    DEFAULT = "permit"

    CHOICES = (
        ("permit", "Permit", "green"),
        ("log", "Log", "cyan"),
        ("deny", "Deny", "orange"),
        ("reject", "Reject", "red"),
    )


class RuleApplicationChoices(ChoiceSet):

    DEFAULT = "any"

    CHOICES = (
        ("any", "Any", "green"),
        ("sql", "SQL", "cyan"),
        ("ssh", "SSH", "orange"),
        ("telnet", "TELNET", "red"),
        ("web", "Web", "green"),
    )


class SecurityPolicy(NetBoxModel):
    comments = models.TextField(blank=True)
    default_action = models.CharField(
        max_length=100, choices=PolicyActionChoices, default=PolicyActionChoices.DEFAULT
    )
    from_zone = models.CharField(max_length=100, choices=SecurityZonesChoices)
    name = models.CharField(max_length=100)
    to_zone = models.CharField(max_length=100, choices=SecurityZonesChoices)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_status_color(self):
        return SecurityZonesChoices.colors.get(self.status)

    def get_absolute_url(self):
        return reverse("plugins:netbox_juniper_srx:securitypolicy", args=[self.pk])


class SecurityPolicyRule(NetBoxModel):
    action = models.CharField(
        max_length=100, choices=RuleActionChoices, default=RuleActionChoices.DEFAULT
    )
    address_source = models.CharField(max_length=30)
    address_destination = models.CharField(max_length=30)
    application = models.CharField(
        max_length=100,
        choices=RuleApplicationChoices,
        default=RuleActionChoices.DEFAULT,
    )
    dynamic_application = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=500, blank=True)
    index = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    security_policy = models.ForeignKey(
        to=SecurityPolicy, on_delete=models.CASCADE, related_name="rules"
    )

    class Meta:
        ordering = ("security_policy", "index")
        unique_together = ("security_policy", "index")

    def __str__(self):
        return f"{self.security_policy}: Rule {self.index}"

    def get_absolute_url(self):
        return reverse("plugins:netbox_juniper_srx:securitypolicyrule", args=[self.pk])
