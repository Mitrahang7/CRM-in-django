
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('client_detail/<int:pk>/', views.client_detail, name='client_detail'),
    path('client_delete/<int:pk>/', views.client_delete, name='client_delete'),
    path('add_client/', views.add_client, name='add_client'),
    path('client_update/<int:pk>/', views.client_update, name='client_update'),
    path('client/<int:client_id>/products/', views.client_products, name='client_products'),
    path('new_product/<int:client_id>/', views.new_product, name='new_product'),
    path('export_clients/', views.export_clients, name='export_clients'),
    path('exoprt_with_pdf/', views.exoprt_with_pdf, name='exoprt_with_pdf'),
    path('search_clients/', views.search_clients, name='search_clients'),
]
