from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


class ZoneStatusChoices(ChoiceSet):

    STATUS_OFFLINE = "offline"
    STATUS_ACTIVE = "active"
    STATUS_PLANNED = "planned"
    STATUS_FAILED = "failed"

    CHOICES = (
        (STATUS_OFFLINE, "Offline", "orange"),
        (STATUS_ACTIVE, "Active", "green"),
        (STATUS_PLANNED, "Planned", "cyan"),
        (STATUS_FAILED, "Failed", "red"),
    )


class InboundProtocolChoices(ChoiceSet):

    ALL = "all"
    BFD = "bfd"
    BGP = "bgp"
    DISCOVERY = "router-discovery"
    DVMRP = "dvmrp"
    IGMP = "igmp"
    LDP = "ldp"
    MSDP = "msdp"
    NDP = "ndp"
    NHRP = "nhrp"
    OSPF = "ospf"
    OSPF3 = "ospf3"
    PGM = "pgm"
    PIM = "pim"
    RIP = "rip"
    RIP_NG = "ripng"
    RSVP = "rsvp"
    SAP = "sap"
    VRRP = "vrrp"

    CHOICES = (
        (ALL, "All", "orange"),
        (BFD, "BFD", "green"),
        (BGP, "BGP", "cyan"),
        (DISCOVERY, "Router-Discovery", "red"),
        (DVMRP, "DVMRP", "orange"),
        (IGMP, "IGMP", "green"),
        (LDP, "LDP", "cyan"),
        (MSDP, "MSDP", "red"),
        (NDP, "NDP", "orange"),
        (NHRP, "NHRP", "green"),
        (OSPF, "OSPF", "cyan"),
        (OSPF3, "OSPFv3", "red"),
        (PGM, "PGM", "orange"),
        (PIM, "PIM", "green"),
        (RIP, "RIP", "cyan"),
        (RIP_NG, "RIP-NG", "red"),
        (RSVP, "RSVP", "orange"),
        (SAP, "SAP", "green"),
        (VRRP, "VRRP", "cyan"),
    )


class InboundServicesChoices(ChoiceSet):

    ALL = "all"
    ANY_SERVICE = "any-service"
    APPQOE = "appqoe"
    BOOTP = "bootp"
    DHCP = "dhcp"
    DHCPV6 = "dhcpv6"
    DNS = "dns"
    FINGER = "finger"
    FTP = "ftp"
    IDENT_RST = "ident-reset"
    HIGH_AVAILABILITY = "high-availability"
    HTTP = "http"
    HTTPS = "https"
    IKE = "ike"
    NETCONF = "netconf"
    PING = "ping"
    RLOGIN = "rlogin"
    RTELNET = "reverse-telnet"
    RSSH = "reverse-ssh"
    RPM = "rpm"
    RSH = "rsh"
    SNMP = "snmp"
    SNMP_TRAP = "snmp-trap"
    SSH = "ssh"
    TELNET = "telnet"
    TRACEROUTE = "traceroute"
    XNM_SSL = "xnm-ssl"
    XNM = "xnm-clear-text"
    TFTP = "tftp"
    LSPING = "lsping"
    LSSELFPING = "lsselfping"
    NTP = "ntp"
    SIP = "sip"
    R2CP = "r2cp"
    WEBAPI = "webapi-clear-text"
    WEBAPI_SSL = "webapi-ssl"
    TCP_ENCAP = "tcp-encap"

    CHOICES = (
        (ALL, "All", "orange"),
        (ANY_SERVICE, "any-service", "green"),
        (APPQOE, "AppQoE", "cyan"),
        (BOOTP, "bootp", "orange"),
        (DHCP, "dhcp", "orange"),
        (DHCPV6, "dhcpv6", "orange"),
        (DNS, "dns", "orange"),
        (FINGER, "finger", "orange"),
        (FTP, "ftp", "orange"),
        (IDENT_RST, "ident-reset", "orange"),
        (HIGH_AVAILABILITY, "high-availability", "orange"),
        (HTTP, "http", "orange"),
        (HTTPS, "https", "orange"),
        (IKE, "ike", "orange"),
        (NETCONF, "netconf", "orange"),
        (PING, "ping", "orange"),
        (RLOGIN, "rlogin", "orange"),
        (RTELNET, "reverse-telnet", "orange"),
        (RSSH, "reverse-ssh", "orange"),
        (RPM, "rpm", "orange"),
        (RSH, "rsh", "orange"),
        (SNMP, "snmp", "orange"),
        (SNMP_TRAP, "snmp-trap", "orange"),
        (SSH, "ssh", "orange"),
        (TELNET, "telnet", "orange"),
        (TRACEROUTE, "traceroute", "orange"),
        (XNM_SSL, "xnm-ssl", "orange"),
        (XNM, "xnm-clear-text", "orange"),
        (TFTP, "tftp", "orange"),
        (LSPING, "lsping", "orange"),
        (LSSELFPING, "lsselfping", "orange"),
        (NTP, "ntp", "orange"),
        (SIP, "sip", "orange"),
        (R2CP, "r2cp", "orange"),
        (WEBAPI, "webapi-clear-text", "orange"),
        (WEBAPI_SSL, "webapi-ssl", "orange"),
        (TCP_ENCAP, "tcp-encap", "orange"),
    )


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


class SecurityBase(NetBoxModel):
    """Our base security object class."""

    device = models.ForeignKey(
        to="dcim.Device",
        on_delete=models.PROTECT,
        related_name="%(class)s_related",
        blank=True,
        null=True,
    )

    description = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True


class SecurityPolicy(SecurityBase):
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


class SecurityPolicyRule(SecurityBase):
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
    comments = models.TextField(blank=True)
    dynamic_application = models.CharField(max_length=30, blank=True)
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


class SecurityZone(SecurityBase):
    comments = models.TextField(blank=True)
    default_action = models.CharField(
        max_length=100, choices=PolicyActionChoices, default=PolicyActionChoices.DEFAULT
    )
    name = models.CharField(max_length=100)
    app_tracking = models.BooleanField(default=False)
    match_interfaces = models.ManyToManyField(
        to="dcim.Interface",
        blank=True,
        related_name="+",
    )
    inbound_protocols = models.CharField(
        max_length=50,
        choices=InboundProtocolChoices,
        default=InboundProtocolChoices.ALL,
    )
    inbound_services = models.CharField(
        max_length=50,
        choices=InboundServicesChoices,
        default=InboundServicesChoices.ALL,
    )
    status = models.CharField(
        max_length=50,
        choices=ZoneStatusChoices,
        default=ZoneStatusChoices.STATUS_ACTIVE,
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_status_color(self):
        return SecurityZonesChoices.colors.get(self.status)

    def get_absolute_url(self):
        return reverse("plugins:netbox_juniper_srx:securityzone", args=[self.pk])
