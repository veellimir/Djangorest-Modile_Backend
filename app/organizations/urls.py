from typing import List

from django.urls import path
from . import views

urlpatterns: List[path] = [
    path('api/organizations/create/', views.OrganizationCreateView.as_view(), name='organizations-create'),
    path('api/organizations/invite/', views.OrganizationInviteView.as_view(), name='organizations-invite'),
    path('api/organizations/list/', views.OrganizationListView.as_view(), name='get_list_organizations'),
]
