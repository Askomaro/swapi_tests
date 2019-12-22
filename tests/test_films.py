from resources.films_resource import FilmsResource

__author__ = 'anton.skomarovskyi@gmail.com'


class TestFilms:
    def test_check_films(self, get_films):
        # arrange
        expected_result = {
            'count': 7,
            'next': None,
            'previous': None,
            'results': get_films
        }
        films_resource = FilmsResource()

        # act
        resp = films_resource.get_all_films()

        # assert
        assert resp == expected_result

    def test_check_film_first(self, get_films):
        # arrange
        expected_result = {
            'count': 7,
            'next': None,
            'previous': None,
            'results': get_films[0]
        }
        films_resource = FilmsResource()

        # act
        resp = films_resource.get_film(1)

        # assert
        assert resp == expected_result
