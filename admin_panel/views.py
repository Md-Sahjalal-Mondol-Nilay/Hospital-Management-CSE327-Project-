from django.shortcuts import render
from django.http import HttpResponse
from admin_panel import forms
from doctor.models import Doctor
from patient.models import Patient

# Create your views here.
def print(request):
    return HttpResponse("Printing From Admin Panel")

#Viewin Home page of The admin
def admin_home(request): # This Function is Showing Home page of Admin Panel
    diction={'title':"Admin Panel"}
    return render(request, 'admin_panel/admin_home.html',context=diction)



# Maintainig Doctors
def doctor_index(request): # It is Viweing Doctor index
    doctor_list = Doctor.objects.order_by('doctor_name')
    
    diction={'title':"Doctor Management",'doctor_list':doctor_list}
    return render(request, 'admin_panel/doctor_index.html',context=diction)


def doctor_form(request): # It is Viweing Doctor index
    form = forms.DoctorForm() # For Variable e Forms.DoctrForm ta niye ashlam

    #Database E Add er Kaj Cholche

    if request.method=="POST":
        form = forms.DoctorForm(request.POST)
        
        if form.is_valid(): # Validity Check kore save kore Dibe
            form.save(commit=True)
            return doctor_index(request)

    diction={'title':"Doctor Mangement","doctor_form":form}
    return render(request, 'admin_panel/doctor_form.html',context=diction)




# Maintaining Patients
def patient_index(request): # It is Viweing Doctor index
    patient_list = Patient.objects.order_by('patient_name')
    
    diction={'title':"Patient Management",'patient_list':patient_list}
    return render(request, 'admin_panel/patient_index.html',context=diction)



def patient_form(request): # It is Viweing Doctor index
    form = forms.PatientForm()
    
    #Database E Add er Kaj Cholche

    if request.method=="POST":
        form = forms.PatientForm(request.POST)
        
        if form.is_valid(): # Validity Check kore save kore Dibe
            form.save(commit=True)
            return patient_index(request)


    diction={'title':"Patient Mangement","patient_form":form}
    return render(request, 'admin_panel/patient_form.html',context=diction)


