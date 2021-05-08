from django.urls import path
from .import views 

# Django Olny looks at Main Url.py


urlpatterns = [
   path('patient_register',views.patient_register,name='patient_register'),
   path('patient_list',views.patient_list,name='patient_list'),  
   path('patient_login',views.patient_login,name='patient_login'),  
   path('patient_logout',views.patient_logout,name='patient_logout'),  
   path('patient_profile/<int:patient_id>',views.patient_profile,name='patient_profile'),  
] 