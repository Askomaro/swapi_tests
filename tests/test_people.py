from builtins import range

import pytest

from helpers.time_execution import time_execution
from resources.people_resource import PeopleResource

__author__ = 'anton.skomarovskyi@gmail.com'


class TestPeople:
    @time_execution
    @pytest.mark.parametrize('id', [id for id in range(1, 88) if id != 17])
    def test_check_person_number_(self, id, get_people):
        # arrange
        expected_result = get_people(id=id)

        films_resource = PeopleResource()

        # act
        resp = films_resource.get_person(id)

        # assert
        assert resp == expected_result

    @time_execution
    def test_check_people_page_number_one(self, get_people):
        # arrange
        expected_result = {
            'count': 87,
            'next': 'https://swapi.co/api/people/?page=2',
            'previous': None,
            'results': get_people()[:10]
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people()

        # assert
        assert resp == expected_result

    @time_execution
    def test_check_people_page_number_two(self, get_people):
        # arrange
        expected_result = {
            'count': 87,
            'next': 'https://swapi.co/api/people/?page=3',
            'previous': 'https://swapi.co/api/people/?page=1',
            'results': [person for person in get_people()[10:21] if person]
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people(page=2)

        # assert
        assert resp == expected_result

    @time_execution
    def test_check_people_page_number_third(self, get_people):
        # arrange
        expected_result = {
            'count': 87,
            'next': 'https://swapi.co/api/people/?page=4',
            'previous': 'https://swapi.co/api/people/?page=2',
            'results': get_people()[21:31]
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people(page=3)

        # assert
        assert resp == expected_result

    @time_execution
    def test_check_people_page_number_fourth(self, get_people):
        # arrange
        expected_result = {
            'count': 87,
            'next': 'https://swapi.co/api/people/?page=5',
            'previous': 'https://swapi.co/api/people/?page=3',
            'results': get_people()[31:34] + get_people()[35:42]
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people(page=4)

        # assert
        assert resp == expected_result

    @time_execution
    def test_check_people_page_number_fifth(self, get_people):
        # arrange
        expected_result = {
            'count': 87,
            'next': 'https://swapi.co/api/people/?page=6',
            'previous': 'https://swapi.co/api/people/?page=4',
            'results': get_people()[42:46] + get_people()[47:53]
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people(page=5)

        # assert
        assert resp == expected_result

    @time_execution
    def test_check_people_page_number_six(self, get_people):
        # arrange
        expected_result = {
            'count': 87,
            'next': 'https://swapi.co/api/people/?page=7',
            'previous': 'https://swapi.co/api/people/?page=5',
            'results': get_people()[53:63]
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people(page=6)

        # assert
        assert resp == expected_result

    @time_execution
    def test_check_people_page_number_seventh(self, get_people):
        # arrange
        expected_result = {
            'count': 87,
            'next': 'https://swapi.co/api/people/?page=8',
            'previous': 'https://swapi.co/api/people/?page=6',
            'results': get_people()[63:73]
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people(page=7)

        # assert
        assert resp == expected_result

    @time_execution
    def test_check_people_page_number_eight(self, get_people):
        # arrange
        expected_result = {
            'count': 87,
            'next': 'https://swapi.co/api/people/?page=9',
            'previous': 'https://swapi.co/api/people/?page=7',
            'results': get_people()[73:74] + get_people()[46:47] + get_people()[74:82]
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people(page=8)

        # assert
        assert resp == expected_result

    @time_execution
    def test_check_people_page_number_ninth(self, get_people):
        # arrange
        people = get_people()[82:]
        people.append(get_people(35))

        expected_result = {
            'count': 87,
            'next': None,
            'previous': 'https://swapi.co/api/people/?page=8',
            'results': people
        }
        people_resource = PeopleResource()

        # act
        resp = people_resource.get_people(page=9)

        # assert
        assert resp == expected_result
