import json

import requests

__author__ = 'anton.skomarovskyi@gmail.com'


class BaseResource:
    def __init__(self):
        pass

    _SCHEMA = 'https://'
    _HOST = 'swapi.co/api/'

    def _get_response(self, url, params=None):
        r = requests.get(url, params=params)

        return json.loads(r.text)
