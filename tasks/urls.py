"""
URL configuration for todoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('', views.TaskListView.as_view(), name='task_list'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    re_path(r'^(?P<pk>[0-9]+)/update/$', views.TaskUpdateView.as_view(), name='task_update'),
    re_path(r'^(?P<pk>[0-9]+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete')
]