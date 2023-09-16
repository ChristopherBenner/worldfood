# dashboard/tests/test_views.py

from django.test import Client
from django.test import TestCase

class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_renders_template(self):
        response = self.client.get('/dashboard/')
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')