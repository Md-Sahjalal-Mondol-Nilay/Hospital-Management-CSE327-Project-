from django.shortcuts import render,redirect
from django.http import HttpResponse
from patient import models
from patient.models import Patient
from patient import forms
from django.contrib.auth.decorators import login_required


# Create your views here.


def patient_register(request):        #Patient_Register

    """
    This method is used to register Patients.
     :param request: it's a HttpResponse from user.
     :type request: HttpResponse.
     :return: this method returns a html page that displays a register form and can submit the form.
     :rtype: HttpResponse.
     
    """
    form= forms.PatientRegisterForm()
    if request.method == 'POST':
        form= forms.PatientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_login')
    return render(request, 'patient/patient_register.html',{'form':form})
   
def patient_login(request):             #Patient_Login

    """
    This method is used to login Patients.
     :param request: it's a HttpResponse from user.
     :type request: HttpResponse.
     :return: this method returns a html page that displays a login form and can submit the form.
     :rtype: HttpResponse.
     
    """
    form= forms.PatientLoginForm()
    if request.method == 'POST':
        form= forms.PatientLoginForm(request.POST)
        patient_email = request.POST.get('patient_email')
        patient_password = request.POST.get('patient_password')
        return redirect('patient_profile')
        return render(request, 'patient/patient_login.html',{'form':form})

def patient_logout(request):                #Patient_Logout

    """
    This method is used to logout Patients.
     :param request: it's a HttpResponse from user.
     :type request: HttpResponse.
     :return: this method returns a html page that displays a home page.
     :rtype: HttpResponse.
     
    """
    form= forms.PatientLogoutForm()
    if request.method == 'POST':
            form= forms.PatientLogoutForm(request.POST)
            patient_email = request.POST.get('patient_email')
            patient_password = request.POST.get('patient_password')
            return redirect('home')
       
def patient_list(request):              #Patient_Lists

    """
    This method is used to show Patient Lists.
     :param request: it's a HttpResponse from user.
     :type request: HttpResponse.
     :return: this method returns a html page that Patient Lists.
     :rtype: HttpResponse.
     
    """
    patient_list = Patient.objects.get(pk=patient_id)
    return render (request,'patient/patient_list.html')

@login_required
def patient_profile(request, patient_id):      #Patient_Profile

    """
    This method is used to show Patient Profile.
     :param request: it's a HttpResponse from user.
     :type request: HttpResponse.
     :return: this method returns a html page that displays Patients Profile.
     :rtype: HttpResponse.
     
    """
    patient_profile = Patient.objects.get(pk=patient_id)
    return render (request,'patient/patient_profile.html')
    
    

   
    