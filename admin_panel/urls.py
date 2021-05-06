from .import views #. mane Current Directory an ai Directory theke Views Ta Import korse
from django.urls import path

# Django Olny looks at Main Url.py

app_name ='admin_panel' #namespacing the URL
urlpatterns = [
   path('',views.print,name='print'),  
] 