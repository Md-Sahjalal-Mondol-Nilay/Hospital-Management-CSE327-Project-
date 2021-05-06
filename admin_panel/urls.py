from admin_panel import views #. mane Current Directory an ai Directory theke Views Ta Import korse
from django.urls import path

# Django Olny looks at Main Url.py

app_name ='admin_panel' #namespacing the URL
urlpatterns = [
   path('admin_home',views.admin_home,name='admin_home'),
   path('doctor_index',views.doctor_index,name='doctor_index'),  
] 