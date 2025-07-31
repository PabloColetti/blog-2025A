from django.urls import path
from apps.user import views as views

app_name = 'user'

urlpatterns = [
    path('users/profile', views.UserProfileView.as_view(), name='user_profile'),
    path('auth/register', views.RegisterView.as_view(), name='auth_register'),
    path('auth/login', views.LoginView.as_view(), name='auth_login'),
    path('auth/logout', views.LogoutView, name='auth_logout'),

]
