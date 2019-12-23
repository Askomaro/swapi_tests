import pytest

from resources.films_resource import FilmsResource

__author__ = 'anton.skomarovskyi@gmail.com'


class TestFilms:
    def test_check_films(self, get_films):
        # arrange
        expected_result = {
            'count': 7,
            'next': None,
            'previous': None,
            'results': get_films()
        }
        films_resource = FilmsResource()

        # act
        resp = films_resource.get_all_films()

        # assert
        assert resp == expected_result

    @pytest.mark.parametrize('id', [1, 2, 3, 4, 5, 6, 7])
    def test_check_film_number_(self, id, get_films):
        # arrange
        expected_result = get_films(id=id)

        films_resource = FilmsResource()

        # act
        resp = films_resource.get_film(id)

        # assert
        assert resp == expected_result
