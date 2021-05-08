from django.shortcuts import render
from django.http import HttpResponse
from admin_panel import forms
from doctor.models import Doctor
from patient.models import Patient




def admin_home(request):
    """
    This method is used to display home page of Admin_panel.


    :param request: it's a HttpResponse from user.


    :type request: HttpResponse.


    :return: this method returns a home page of the admin_panel
     which is a HTML page.


    :rtype: HttpResponse.
    """
    diction={'title':"Admin Panel"}
    return render(request, 'admin_panel/admin_home.html',context=diction)



    """
     From Here Managing Doctors part Started.

    """
def doctor_index(request): # It is Viweing Doctor index
    """
     This method is used to display the Doctor list.

     :param request: it's a HttpResponse from user.

     :type request: HttpResponse.

     :return: this method returns a html page that display all the Doctors 
      available.

     :rtype: HttpResponse.
     
     """
    doctor_list = Doctor.objects.order_by('doctor_name')

    diction={'title':"Doctor Management",'doctor_list':doctor_list}
    return render(request, 'admin_panel/doctor_index.html',context=diction)




def doctor_form(request):
    """
     This method is used to Add  Doctor via Form.

     :param request: it's a HttpResponse from user.

     :type request: HttpResponse.

     :return: this method returns a html page that  allows user to add 
     
     Doctors.
    
     :rtype: HttpResponse.
     
     """
    form = forms.DoctorForm() 
    if request.method=="POST":
        form = forms.DoctorForm(request.POST)   
        if form.is_valid(): # Validity Check kore save kore Dibe
            form.save(commit=True)
            return doctor_index(request)
    diction={'title':"Doctor Mangement","doctor_form":form}
    return render(request, 'admin_panel/doctor_form.html',context=diction)



def doctor_info(request,doctor_id):
    """
     This method is used to View Indivdual Doctor after getting from their unique 
     primary key.

     :param request: it's a HttpResponse from user and Doctor primary key from the 
      databae.

     :type request: HttpResponse.

     :return: this method returns a html page that display information of an 
     
     individual Doctor.
           
     :rtype: HttpResponse.
     
     """
    doctor_info =Doctor.objects.get(pk=doctor_id)
    diction = {'doctor_info':doctor_info}
    return render(request, 'admin_panel/doctor_info.html',context =diction)




def doctor_update(request,doctor_id):
    """
     This method is used to Update each Doctor according to their  unique primary
     key.

     :param request: it's a HttpResponse from user and Doctor primary key from the 
      databae.

     :type request: HttpResponse.

     :return: this method returns a html page that update information of an 
     
     individual Doctor.
           
     :rtype: HttpResponse.
     
     """
    doctor_info =Doctor.objects.get(pk=doctor_id)
    
    form = forms.DoctorForm(instance=doctor_info)
    if request.method=="POST":
        form=forms.DoctorForm(request.POST,instance=doctor_info)
        if form.is_valid(): 
            form.save(commit=True)
            return doctor_index(request)
    diction = {'doctor_form':form}
    return render(request, 'admin_panel/doctor_update.html',context =diction)




def doctor_delete(request,doctor_id):
    """
     This method is used to Delete each Doctor according to their  unique primary
     key.

     :param request: it's a HttpResponse from user and Doctor primary key from the 
      databae.

     :type request: HttpResponse.

     :return: this method returns a html page that delete information of an 
     
     individual Doctor.
           
     :rtype: HttpResponse.
     
     """
    doctor =Doctor.objects.get(pk=doctor_id).delete()
    diction = {'delete_message': "Delete Done"}
    return render(request, 'admin_panel/doctor_delete.html',context =diction)


"""
     From Here Managing Patients part Started.

"""
def patient_index(request): 
    """
     This method is used to display the Patient list.

     :param request: it's a HttpResponse from user.

     :type request: HttpResponse.

     :return: this method returns a html page that display all the Patients 
      available.

     :rtype: HttpResponse.
     
    """
    patient_list = Patient.objects.order_by('patient_name')
    diction={'title':"Patient Management",'patient_list':patient_list}
    return render(request, 'admin_panel/patient_index.html',context=diction)



def patient_form(request):
    """
     This method is used to Add  Patient via Form.

     :param request: it's a HttpResponse from user.

     :type request: HttpResponse.

     :return: this method returns a html page that  allows user to add 
     
     Patients.
    
     :rtype: HttpResponse.
     
    """
    form = forms.PatientForm()
    if request.method=="POST":
        form = forms.PatientForm(request.POST)
        if form.is_valid(): # Validity Check kore save kore Dibe
            form.save(commit=True)
            return patient_index(request)
    diction={'title':"Patient Mangement","patient_form":form}
    return render(request, 'admin_panel/patient_form.html',context=diction)



def patient_info(request,patient_id):
    """
     This method is used to View Indivdual Patient after getting from their unique 
     primary key.

     :param request: it's a HttpResponse from user and Patient primary key from the 
      databae.

     :type request: HttpResponse.

     :return: this method returns a html page that display information of an 
     
     individual Patient.
           
     :rtype: HttpResponse.
     
    """
    patient_info =Patient.objects.get(pk=patient_id)
    diction = {'patient_info':patient_info}
    return render(request, 'admin_panel/patient_info.html',context =diction)



def patient_update(request,patient_id):
    """
     This method is used to Update each Patient according to their  unique primary
     key.

     :param request: it's a HttpResponse from user and Patient primary key from the 
      databae.

     :type request: HttpResponse.

     :return: this method returns a html page that update information of an 
     
     individual Patient.
           
     :rtype: HttpResponse.
     
    """
    patient_info =Patient.objects.get(pk=patient_id)
    form = forms.PatientForm(instance=patient_info)
    if request.method=="POST":
        form=forms.PatientForm(request.POST,instance=patient_info)
        if form.is_valid():
            form.save(commit=True)
            return patient_index(request)
    diction = {'patient_form':form}
    return render(request, 'admin_panel/patient_update.html',context =diction)





def patient_delete(request,patient_id):
    """
     This method is used to Delete each Patient according to their  unique primary
     key.

     :param request: it's a HttpResponse from user and Patient primary key from the 
      databae.

     :type request: HttpResponse.

     :return: this method returns a html page that delete information of an 
     
     individual Patient.
           
     :rtype: HttpResponse.
     
    """
    patient =Patient.objects.get(pk=patient_id).delete()
    diction = {'delete_message': "Delete Done"}
    return render(request,'admin_panel/patient_delete.html',context =diction)