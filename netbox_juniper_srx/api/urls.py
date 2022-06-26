from netbox.api.routers import NetBoxRouter
from . import views


app_name = "netbox_juniper_srx"


router = NetBoxRouter()
router.register("policies", views.SecurityPolicyViewSet)
router.register("policy-rules", views.SecurityPolicyRuleViewSet)
router.register("zones", views.SecurityZoneViewSet)

urlpatterns = router.urls
