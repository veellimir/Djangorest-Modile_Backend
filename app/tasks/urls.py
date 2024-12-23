from typing import List

from django.urls import path
from . import views

urlpatterns: List[path] = [
    path('api/tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('api/tasks/list/', views.TasksOrganizationView.as_view(), name='task-list'),
    path('api/tasks/status/', views.TasksStatusesListView.as_view(), ),
]
