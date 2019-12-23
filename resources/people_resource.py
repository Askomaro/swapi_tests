from resources.base_resource import BaseResource


class PeopleResource(BaseResource):
    _URL_API_PATH = 'people'

    def __init__(self):
        BaseResource.__init__(self)
        self.__url_path = "%s%s%s" % (self._SCHEMA,
                                      self._HOST,
                                      self._URL_API_PATH)

    def get_people(self):
        return self._get_response(self.__url_path)

    def get_person(self, person_id):
        return self._get_response('%s/%s' % (self.__url_path, person_id))
