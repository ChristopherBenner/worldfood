# dashboard/tests/test_views.py

from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
class DashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_view_renders_template(self):
        response = self.client.get('/dashboard/')
        self.assertTemplateUsed(response, 'dashboard/dashboard.html')

    def test_view_saved_recipes_renders_templates(self):
        response = self.client.get('/dashboard/saved-recipes/')
        self.assertTemplateUsed(response, 'dashboard/saved_recipes.html')