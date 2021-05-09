from django.test import SimpleTestCase
from django.urls import reverse,resolve

from doctor.views import doctor_authentication,doctor_signup,doctor_login

class TestUrls(SimpleTestCase):

    def test_doctor_authentication_url_is_resolved(self):
        url = reverse('doctor:doctor_authentication')
        print(resolve(url))
        self.assertEquals(resolve(url).func,doctor_authentication)

    def test_doctor_signup_url_is_resolved(self):
        url = reverse('doctor:doctor_signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func,doctor_signup)

    def test_doctor_login_url_is_resolved(self):
        url = reverse('doctor:doctor_login')
        print(resolve(url))
        self.assertEquals(resolve(url).func,doctor_login)
        