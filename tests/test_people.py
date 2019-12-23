from builtins import range

import pytest

from resources.people_resource import PeopleResource

__author__ = 'anton.skomarovskyi@gmail.com'


class TestPeople:
    def test_check_people(self, get_people):
        # arrange
        expected_result = {
            'count': 7,
            'next': None,
            'previous': None,
            'results': get_people
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people()

        # assert
        assert resp == expected_result

    @pytest.mark.parametrize('id', [id for id in range(1, 88) if id != 17])
    def test_check_person_number_(self, id, get_people):
        # arrange
        expected_result = get_people(id=id)

        films_resource = PeopleResource()

        # act
        resp = films_resource.get_person(id)

        # assert
        assert resp == expected_result
