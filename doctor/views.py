from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse


def doctor_authentication(request):
    """
    This method is used to show authentacion page.


    :param request: it's a HttpResponse from doctor.


    :type request: HttpResponse.


    :return: this method returns signup and login page after successfully
    submit.


    :rtype: HttpResponse.
    """
    diction = {} 
    return render(request, 'doctor/doctor_authentication.html', context=diction)

def doctor_login(request):
    """
    This method is used to login a doctor.


    :param request: it's a HttpResponse from doctor.


    :type request: HttpResponse.


    :return: this method returns a  login page after successfully
    submit.


    :rtype: HttpResponse.
    """

    if request.method == "POST":
        doctor_name = request.POST['doctor_name']
        doctor_password = request.POST['doctor_password']

        user = auth.authenticate(doctor_name=doctor_name, doctor_password=doctor_password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'doctor/doctor_authentication.html')

    return render(request, 'doctor/doctor_login.html')
    

def doctor_signup(request):    
    """
    This method is used to signup a doctor.


    :param request: it's a HttpResponse from doctor.


    :type request: HttpResponse.


    :return: this method returns a  authentication page after successfull
    registration.
    

    :rtype: HttpResponse.
    """

    if request.method == 'POST':
        doctor_name = request.POST['doctor_name']
        doctor_email = request.POST['doctor_email']
        doctor_password = request.POST['doctor_password']
        doctor_gender = request.POST['doctor_gender']
        doctor_visitng_hour = request.POST['doctor_visitng_hour']
        doctor_room_number = request.POST['doctor_room_number']

        user = User.objects.create_user(doctor_name = doctor_name, doctor_email = doctor_email, doctor_password = doctor_password, doctor_gender = doctor_gender, doctor_visitng_hour = doctor_visitng_hour, doctor_room_number = doctor_room_number)
        user.save()
        print('Successfully Registered')
        return redirect('doctor/doctor_authentication.html')
    else:
        return render(request, 'doctor/doctor_signup.html')




    