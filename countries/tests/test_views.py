# countries/tests/view_test.py

from django.test import Client
from django.test import TestCase

from ..models import Continent, Country

class CountryListViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_renders_template(self):
        response = self.client.get('/countries/')
        self.assertTemplateUsed(response, 'countries/countries_homepage.html') 
        self.assertEqual(response.status_code, 200)

    def test_view_returns_continents_list(self):
        continent = Continent.objects.create(name='Asia')
        #country = Country.objects.create(name='Afghanistan', continent=continent)
        response = self.client.get('/countries/')
        self.assertListEqual(response.context['continents'], [continent])

    def test_view_returns_countries_list(self):
        continent = Continent.objects.create(name='Asia')
        country = Country.objects.create(name='Afghanistan', continent=continent)
        response = self.client.get('/countries/')
        self.assertListEqual(response.context['countries'], [country])


    