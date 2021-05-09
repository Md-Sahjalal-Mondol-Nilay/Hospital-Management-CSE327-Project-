from django import forms
from patient import models

class PatientRegisterForm(forms.ModelForm): #It will create the Patient_Registration_Form
   class Meta:
       model = models.Patient
       fields = "__all__"

class PatientLoginForm(forms.ModelForm): #It will create the Patient_Login_Form
    class Meta:
        model = models.Patient
        fields = ['patient_email', 'patient_password']

class PatientLogoutForm(forms.ModelForm): #It will create the Patient_Logout_Form
    class Meta:
        model = models.Patient
        fields = ['patient_email', 'patient_password']

