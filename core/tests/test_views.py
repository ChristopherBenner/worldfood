# cores/tests/test_views.py

from django.test import Client
from django.test import TestCase, RequestFactory

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_renders_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'core/home.html')

    