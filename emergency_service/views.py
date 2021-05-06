from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print(request):
    return HttpResponse("Printing From Emergency Service")