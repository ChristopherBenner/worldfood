# cores/tests/test_views.py

from django.test import Client
from django.test import TestCase, RequestFactory
from django.urls import reverse

from ..forms import SignUpForm

class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_renders_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'core/home.html')

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_renders_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'core/login.html')

class SignupViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_renders_template(self):
        response = self.client.get('/signup/')
        self.assertTemplateUsed(response, 'core/signup.html')

    def test_redirects_to_login(self):
        form_data = {'username': 'test',
                     'email': 'test@test.com',
                     'password1': 'testpassword',
                     'password2': 'testpassword',}
        
        form = SignUpForm(form_data)

        response = self.client.post('/signup/', form_data)
        self.assertRedirects(response, reverse('core:login'), status_code=302, target_status_code=200, fetch_redirect_response=True)