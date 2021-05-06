from django.shortcuts import render
from django.http import HttpResponse
from admin_panel import forms

# Create your views here.
def print(request):
    return HttpResponse("Printing From Admin Panel")

#Viewin Home page of The admin
def admin_home(request): # This Function is Showing Home page of Admin Panel
    diction={'title':"Admin Panel"}
    return render(request, 'admin_panel/admin_home.html',context=diction)



# Maintainig Doctors
def doctor_index(request): # It is Viweing Doctor index
    diction={'title':"Doctor Management"}
    return render(request, 'admin_panel/doctor_index.html',context=diction)


def doctor_form(request): # It is Viweing Doctor index
    form = forms.DoctorForm() # For Variable e Forms.DoctrForm ta niye ashlam
    diction={'title':"Doctor Mangement","doctor_form":form}
    return render(request, 'admin_panel/doctor_form.html',context=diction)




# Maintaining Patients
def patient_index(request): # It is Viweing Doctor index
    diction={'title':"Patient Mangement"}
    return render(request, 'admin_panel/patient_index.html',context=diction)

def patient_form(request): # It is Viweing Doctor index
    form = forms.PatientForm()
    diction={'title':"Patient Mangement","patient_form":form}
    return render(request, 'admin_panel/patient_form.html',context=diction)


