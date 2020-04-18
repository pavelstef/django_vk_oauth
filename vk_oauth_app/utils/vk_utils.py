""" Utilities for working with VK Oauth and VK API """


import vk
from requests.exceptions import ConnectionError


DEFAULT_API_VERSION = '5.52'


def get_vk_oauth2_token(user):
    """
    Getting and return a token for VK API
    from user's extra information in the DB
    """
    social = user.social_auth.get(id=user.id)
    return social.extra_data.get('access_token')


def get_vk_oauth2_uid(user):
    """ Getting and return a VK UID from user's extra information in the DB """
    social = user.social_auth.get(id=user.id)
    return social.extra_data.get('uid')


class VkUser:
    """ A class that describes the user of the VK social network  """

    __slots__ = ('_uid', '_session', '_api')

    def __init__(self, uid=None, token=None, api_version=None):
        self._uid = uid
        self._session = vk.Session(access_token=token)
        self._api = vk.API(
            self._session,
            v=(api_version or DEFAULT_API_VERSION),
            lang='ru'
        )

    def get_uid(self):
        """ Returns self VK UID """
        return self._uid

    def get_full_name(self):
        """ Getting user's general information like first name and last name """
        try:
            data = self._api.users.get(user_ids=self._uid)[0]
        except ConnectionError:
            data = {}
        return {'first_name': data.get('first_name'), 'last_name': data.get('last_name')}

    def get_friends(self, count=5):
        """ Getting list of random friends. Returns 5 friends by default """
        fields_list = ['city']
        try:
            data = self._api.friends.get(user_id=self._uid, order='random',
                                         count=count, fields=fields_list)
        except ConnectionError:
            data = {}
        return data
