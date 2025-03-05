
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
]
