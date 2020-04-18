""" Views of application vk_oauth_app """

from django.views import View
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from .utils.vk_utils import get_vk_oauth2_token, get_vk_oauth2_uid, VkUser


class AuthLognView(View):
    """ VK Oauth login view """

    def get(self, request):
        return render(request, 'vk_oauth_app/vk_oauth_login.html')


class HomeView(LoginRequiredMixin, View):
    """
     View which provide home page of app.
     The View prints a greeting for an authorized user
     and show a list of 5 user's friends.
    """

    def get(self, request):
        vk_token = get_vk_oauth2_token(request.user)
        vk_uid = get_vk_oauth2_uid(request.user)
        vk_user = VkUser(token=vk_token, uid=vk_uid)
        context = {
            'full_name': vk_user.get_full_name(),
            'friends': vk_user.get_friends(),
        }
        return render(request, 'vk_oauth_app/vk_oauth_home.html', context=context)
