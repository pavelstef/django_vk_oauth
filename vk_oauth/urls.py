"""vk_oauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
# path('admin/', admin.site.urls),

from django.urls import path, include
from .views import redirect_vk_oauth_app_home, redirect_vk_oauth_app_login

urlpatterns = [
    path('', redirect_vk_oauth_app_home),
    path('accounts/login/', redirect_vk_oauth_app_login),
    path('social/', include('social_django.urls')),
    path('vk_oauth/', include('vk_oauth_app.urls')),

]
