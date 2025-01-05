from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login_tenant/', views.login_tenant, name='login_tenant'),
    path('register_tenant/', views.register_tenant, name='register_tenant'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('edit_admin_info/', views.edit_admin_info, name='edit_admin_info'),
    path('add_house/', views.add_house, name='add_house'),
    path('edit_houses/', views.view_houses, name='edit_houses'),
    path('manage_houses/', views.manage_houses, name='manage_houses'),
    path('admin_edit_tenant/', views.admin_edit_tenant, name='admin_edit_tenant'),
    path('edit_tenant_password_admin/', views.edit_tenant_password_admin, name='edit_tenant_password_admin'),

    path('tenant_home/', views.tenant_home, name='tenant_home'),
    path('edit_tenant_info/', views.edit_tenant_info, name='edit_tenant_info'),
    path('edit_tenant_password/', views.edit_tenant_password, name='edit_tenant_password'),
    path('view_houses/', views.view_houses, name='view_houses'),
    path('search_and_rent/', views.search_and_rent, name='search_and_rent'),
    path('rent_confirmation/', views.rent_confirmation, name='rent_confirmation'),
]
#  search_and_rent
