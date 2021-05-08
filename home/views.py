from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    This method is used to display home page.


    :param request: it's a HttpResponse from user.


    :type request: HttpResponse.


    :return: this method returns a home page
     which is a HTML page.


    :rtype: HttpResponse.
    """
    diction={'title':"Hospital Mangement"}
    return render(request, 'home/home.html',context=diction)
