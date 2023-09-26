# notifications/tests/test_views.py

from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User

class NotificationsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_view_renders_template(self):
        response = self.client.get('/notifications/')
        self.assertTemplateUsed(response, 'notifications/notifications.html')