from django import forms
from doctor import models as doctor_model
from patient import models as patient_model

class DoctorForm(forms.ModelForm): # Ei Class Ta Doctor Table er Jonno Form Create Kortese#
    class Meta:
        model = doctor_model.Doctor
        fields = "__all__"


class PatientForm(forms.ModelForm): # Ei Class Ta Doctor Table er Jonno Form Create Kortese
    class Meta:
        model = patient_model.Patient
        fields = "__all__"