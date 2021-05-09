from django.shortcuts import render

# Create your views here.
#class based views
def index(request):
    return render(request, 'hospital/index.html')