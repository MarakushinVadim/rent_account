from django.urls import path

from rent.views import BaseView, CompanyCreateView, ContainerCreateView, ContainerListView

app_name = 'rent'

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('company_create', CompanyCreateView.as_view(), name='company_create'),
    path('container_create', ContainerCreateView.as_view(), name='container_create'),
    path('container_list', ContainerListView.as_view(), name='container_list'),
]