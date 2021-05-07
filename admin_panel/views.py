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



def doctor_info(request,doctor_id):
    doctor_info =Doctor.objects.get(pk=doctor_id)
    diction = {'doctor_info':doctor_info}
    return render(request, 'admin_panel/doctor_info.html',context =diction)

def doctor_update(request,doctor_id):
    doctor_info =Doctor.objects.get(pk=doctor_id)
    # Update Korar Jonno ekta Form Dorkar amra akhon Shei Form ta banbo
    form = forms.DoctorForm(instance=doctor_info)

    if request.method=="POST":
        form=forms.DoctorForm(request.POST,instance=doctor_info)

        if form.is_valid(): # Validity Check kore save kore Dibe
            form.save(commit=True)
            return doctor_index(request)


    diction = {'doctor_form':form}
    return render(request, 'admin_panel/doctor_update.html',context =diction)












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


def patient_info(request,patient_id):
    patient_info =Patient.objects.get(pk=patient_id)
    diction = {'patient_info':patient_info}
    return render(request, 'admin_panel/patient_info.html',context =diction)



def patient_update(request,patient_id):
    patient_info =Patient.objects.get(pk=patient_id)
    # Update Korar Jonno ekta Form Dorkar amra akhon Shei Form ta banbo
    form = forms.PatientForm(instance=patient_info)

    if request.method=="POST":
        form=forms.PatientForm(request.POST,instance=patient_info)

        if form.is_valid(): # Validity Check kore save kore Dibe
            form.save(commit=True)
            return patient_index(request)


    diction = {'patient_form':form}
    return render(request, 'admin_panel/patient_update.html',context =diction)


