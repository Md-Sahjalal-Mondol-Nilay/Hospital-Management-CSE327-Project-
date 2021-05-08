from django.urls import path
from doctor import views 

# Django Olny looks at Main Url.py

app_name = "doctor"

urlpatterns = [
   path('doctor_authentication',views.doctor_authentication,name='doctor_authentication'),
   path('doctor_signup',views.doctor_signup,name='doctor_signup'), 
   path('doctor_login',views.doctor_login,name='doctor_login'), 


     
] 