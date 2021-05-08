from django import forms
from patient import models
class PatientRegisterForm(forms.ModelForm):
   class Meta:
       model = models.Patient
       fields = "__all__"

class PatientLoginForm(forms.ModelForm): 
    class Meta:
        model = models.Patient
        fields = ['patient_email', 'patient_password']

class PatientLogoutForm(forms.ModelForm): 
    class Meta:
        model = models.Patient
        fields = ['patient_email', 'patient_password']

