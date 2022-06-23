from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    # Security Policies
    path('policies/', views.SecurityPolicyListView.as_view(), name='securitypolicy_list'),
    path('policies/add/', views.SecurityPolicyEditView.as_view(), name='securitypolicy_add'),
    path('policies/<int:pk>/', views.SecurityPolicyView.as_view(), name='securitypolicy'),
    path('policies/<int:pk>/edit/', views.SecurityPolicyEditView.as_view(), name='securitypolicy_edit'),
    path('policies/<int:pk>/delete/', views.SecurityPolicyDeleteView.as_view(), name='securitypolicy_delete'),
    path('policies/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='securitypolicy_changelog', kwargs={'model': models.SecurityPolicy}),

    # Security Policy rules
    path('policy-rules/', views.SecurityPolicyRuleListView.as_view(), name='securitypolicyrule_list'),
    path('policy-rules/add/', views.SecurityPolicyRuleEditView.as_view(), name='securitypolicyrule_add'),
    path('policy-rules/<int:pk>/', views.SecurityPolicyRuleView.as_view(), name='securitypolicyrule'),
    path('policy-rules/<int:pk>/edit/', views.SecurityPolicyRuleEditView.as_view(), name='securitypolicyrule_edit'),
    path('policy-rules/<int:pk>/delete/', views.SecurityPolicyRuleDeleteView.as_view(), name='securitypolicyrule_delete'),
    path('policy-rules/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='securitypolicyrule_changelog', kwargs={'model': models.SecurityPolicyRule}),

)
