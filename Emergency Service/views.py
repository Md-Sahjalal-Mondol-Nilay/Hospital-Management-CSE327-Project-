from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import detail
from django.views.generic.list import ListView
# Create your views here.




@login_required

def detail_view(request):
    detail_view = detail.objects.all()
    context = {
        'detail_view' : detail_view
    }
    return render(request, 'registration/detail.html', context)