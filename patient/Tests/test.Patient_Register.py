from django.test import TestCase
from django.urls import reverse
from patient import models
from patient import forms
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from authentication.utils import generate_token

#Create your TestCase

class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('patient_register')
        self.user={

            'email':'testemail@gmail.com',
            'username':'username',
            'password':'password',
            'password2':'password',
        }
        self.user_short_password={

            'email':'testemail@gmail.com',
            'username':'username',
            'password':'tes',
            'password2':'tes',
        }
        self.user_unmatching_password={

            'email':'testemail@gmail.com',
            'username':'username',
            'password':'teslatt',
            'password2':'teslatto',
        }

        self.user_invalid_email={
            
            'email':'test.com',
            'username':'username',
            'password':'teslatt',
            'password2':'teslatto',
        }
        return super().setUp()

class PatientRegisterTest(BaseTest):

   def test_can_view_page_correctly(self):                 #testing the page of the patient urls
       response=self.patient.get(self.register_url)
       self.assertEqual(response.status_code,200)
       self.assertTemplateUsed(response,'patient/patient_register.html')

   def test_can_register_user(self):                        #testing patient register
        response=self.patient.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

   def test_cant_register_user_withshortpassword(self):      #testing short password authentication
        response=self.patient.post(self.register_url,self.user_short_password,format='text/html')
        self.assertEqual(response.status_code,400)

   def test_cant_register_user_with_unmatching_passwords(self):      #testing unmatching password authentication
        response=self.patient.post(self.register_url,self.user_unmatching_password,format='text/html')
        self.assertEqual(response.status_code,400)

   def test_cant_register_user_with_invalid_email(self):            #testing invalid email id authentication
        response=self.patient.post(self.register_url,self.user_invalid_email,format='text/html')
        self.assertEqual(response.status_code,400)

   def test_cant_register_user_with_taken_email(self):            #testing taken email id authentication
        self.patient.post(self.register_url,self.user,format='text/html')
        response=self.patient.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,400)

