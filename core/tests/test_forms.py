# core/tests/test_forms.py

from django.test import TestCase
from ..forms import LoginForm, SignUpForm

class LoginFormTest(TestCase):
    def test_form_has_required_fields(self):
        form = LoginForm()
        self.assertIn('id="id_username"', form.as_p())
        self.assertIn('id="id_password"', form.as_p())

class SignupFormTest(TestCase):
    def test_form_has_required_field(self):
        form = SignUpForm()
        self.assertIn('id="id_username"', form.as_p())
        self.assertIn('id="id_email"', form.as_p())
        self.assertIn('id="id_password1"', form.as_p())
        self.assertIn('id="id_password2"', form.as_p())