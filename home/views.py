from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    diction={'title':"Hospital Mangement"} # Browser e Tab e Lekha uthbe
    return render(request, 'home/home.html',context=diction)
