from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.AuthLognView.as_view(), name='url_vk_oauth_app_login'),
    path('home/', views.HomeView.as_view(), name='url_vk_oauth_app_home')
]
