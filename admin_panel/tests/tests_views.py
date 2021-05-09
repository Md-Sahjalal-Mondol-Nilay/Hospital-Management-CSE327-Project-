from django.test import TestCase, Client
from django.urls import reverse
from doctor.models import Doctor
from patient.models import Patient
from django.urls import path, re_path
import json

class TestView(TestCase):

    def setUp(self): # Tihs function will goin to run for every single test method.
        self.client=Client()
        
    
    def test_admin_home_GET(self):
        response = self.client.get(reverse('admin_panel:admin_home')) # Test Code
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'admin_panel/admin_home.html')
    
    
    def test_doctor_index_GET(self):
        response = self.client.get(reverse('admin_panel:doctor_index')) # Test Code
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'admin_panel/doctor_index.html')
    
    
    def test_doctor_form_GET(self):
        response = self.client.get(reverse('admin_panel:doctor_form')) # Test Code
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'admin_panel/doctor_form.html')
    
    def test_patient_index_GET(self):
        response = self.client.get(reverse('admin_panel:patient_index')) # Test Code
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'admin_panel/patient_index.html')
    
    
    def test_patient_form_GET(self):
        response = self.client.get(reverse('admin_panel:patient_form')) # Test Code
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'admin_panel/patient_form.html')
    
    

    
    
    

    



# py manage.py test admin_panel


