from django.shortcuts import redirect


def redirect_vk_oauth_app_home(request):
    return redirect('url_vk_oauth_app_home', permanent=True)

def redirect_vk_oauth_app_login(request):
    return redirect('url_vk_oauth_app_login', permanent=True)