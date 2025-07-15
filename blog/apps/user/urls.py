from django.urls import path
from apps.user import views as views

app_name = 'user'

urlpatterns = [
    path('users/profile', views.UserProfileView.as_view(), name='user_profile')
]