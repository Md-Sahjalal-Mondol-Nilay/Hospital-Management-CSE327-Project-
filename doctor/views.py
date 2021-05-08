from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
#from django.http import HttpResponse

# view from doctor 
def doctor_authentication(request):
    diction = {}
    return render(request, 'doctor/doctor_authentication.html', context=diction)

def doctor_login(request):

     return render(request, 'doctor/doctor_login.html')


#view from doctor signup form
def doctor_signup(request):

    if request.method == 'POST':
        doctor_name = request.POST['doctor_name']
        doctor_email = request.POST['doctor_email']
        doctor_password = request.POST['doctor_password']
        doctor_gender = request.POST['doctor_gender']
        doctor_visitng_hour = request.POST['doctor_visitng_hour']
        doctor_room_number = request.POST['doctor_room_number']

        user = User.objects.create_user(doctor_name = doctor_name, doctor_email = doctor_email, doctor_password = doctor_password, doctor_gender = doctor_gender, doctor_visitng_hour = doctor_visitng_hour, doctor_room_number = doctor_room_number)
        user.save();
        print('Successfully Registered')
        return redirect('doctor/doctor_authentication.html')
    else:
        return render(request, 'doctor/doctor_signup.html')




    