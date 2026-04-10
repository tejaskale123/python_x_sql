from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('users/', views.users_list, name='users'),
    path('delete/<int:id>/', views.delete_user, name='delete'),
    path('update/<int:id>/', views.update_user, name='update'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('api/users/', views.api_users),
    path('api/create-user/', views.api_create_user),
    path('api/update-user/<int:id>/', views.api_update_user),
    path('api/delete-user/<int:id>/', views.api_delete_user),
    path('api/login/', views.api_login),
]