from django.test import SimpleTestCase
from django.urls import reverse,resolve

from admin_panel.views import admin_home,doctor_index,doctor_form,doctor_info,doctor_update,doctor_delete,patient_index,patient_form,patient_info,patient_update,patient_delete

class TestUrls(SimpleTestCase):

    def test_admin_home_url_is_resolved(self):
        url = reverse('admin_panel:admin_home')
        print(resolve(url))
        self.assertEquals(resolve(url).func,admin_home)
    
    def test_doctor_index_url_is_resolved(self):
        url = reverse('admin_panel:doctor_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func,doctor_index)
    
    
    def test_doctor_form_url_is_resolved(self):
        url = reverse('admin_panel:doctor_form')
        print(resolve(url))
        self.assertEquals(resolve(url).func,doctor_form)
    
    def test_patient_index_url_is_resolved(self):
        url = reverse('admin_panel:patient_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func,patient_index)
    
    
    
    
    def test_patient_form_url_is_resolved(self):
        url = reverse('admin_panel:patient_form')
        print(resolve(url))
        self.assertEquals(resolve(url).func,patient_form)