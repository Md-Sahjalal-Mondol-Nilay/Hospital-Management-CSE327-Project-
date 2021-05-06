from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print(request):
    return HttpResponse("Printing From Admin Panel")

#Viewin Home page of The admin

def admin_home(request): # This Function is Showing Home page of Admin Panel
    diction={}
    return render(request, 'admin_panel/admin_home.html',context=diction)


def doctor_index(request): # It is Viweing Doctor index
    diction={}
    return render(request, 'admin_panel/doctor_index.html',context=diction)