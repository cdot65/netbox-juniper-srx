from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


class SecurityPolicy(NetBoxModel):
    comments = models.TextField(blank=True)
    default_action = models.CharField(max_length=100)
    from_zone = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    to_zone = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_juniper_srx:securitypolicy", args=[self.pk])


class SecurityPolicyRule(NetBoxModel):
    action = models.CharField(max_length=30)
    address_source = models.CharField(max_length=30)
    address_destination = models.CharField(max_length=30)
    application = models.CharField(max_length=30)
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
