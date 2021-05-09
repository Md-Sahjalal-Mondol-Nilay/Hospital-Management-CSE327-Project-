from django.urls import path
from .import views 

# Django Olny looks at Main Url.py


urlpatterns = [
   path('',views.print,name='print'),  
] 