from django.shortcuts import render,redirect
from django.http import HttpResponse
from patient import models
from patient.models import Patient
from patient import forms
from django.contrib.auth.decorators import login_required


# Create your views here.

def print(request):
    return HttpResponse("Printing From Patient")

def patient_register(request):
    form= forms.PatientRegisterForm()
    if request.method == 'POST':
        form= forms.PatientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_login')
    return render(request, 'patient/patient_register.html',{'form':form})
   
def patient_login(request):
    form= forms.PatientLoginForm()
    if request.method == 'POST':
        form= forms.PatientLoginForm(request.POST)
        patient_email = request.POST.get('patient_email')
        patient_password = request.POST.get('patient_password')
        return redirect('patient_profile')
    return render(request, 'patient/patient_login.html',{'form':form})

def patient_logout(request):
        form= forms.PatientLogoutForm()
        if request.method == 'POST':
            form= forms.PatientLogoutForm(request.POST)
        patient_email = request.POST.get('patient_email')
        patient_password = request.POST.get('patient_password')
        return redirect('home')
        #return render(request, 'home',{'form':form})

def patient_list(request):
    patient_list = Patient.objects.get(pk=patient_id)
    return render (request,'patient/patient_list.html')

@login_required
def patient_profile(request, patient_id):
    patient_profile = Patient.objects.get(pk=patient_id)
    return render (request,'patient/patient_profile.html')
    
    

   
    