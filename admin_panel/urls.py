from admin_panel import views #. mane Current Directory an ai Directory theke Views Ta Import korse
from django.urls import path

# Django Olny looks at Main Url.py

app_name ='admin_panel' #namespacing the URL
urlpatterns = [
   path('admin_home',views.admin_home,name='admin_home'),

   path('doctor_index',views.doctor_index,name='doctor_index'),
   path('doctor_form',views.doctor_form,name='doctor_form'),
   path('doctor_info/<int:doctor_id>/',views.doctor_info,name='doctor_info'),
   path('doctor_update/<int:doctor_id>/',views.doctor_update,name='doctor_update'),
   path('doctor_delete/<int:doctor_id>/',views.doctor_delete,name='doctor_delete'),
   
   
   path('patient_index',views.patient_index,name='patient_index'),
   path('patient_form',views.patient_form,name='patient_form'),
   path('patient_info/<int:patient_id>/',views.patient_info,name='patient_info'),
   path('patient_update/<int:patient_id>/',views.patient_update,name='patient_update'),
   path('patient_delete/<int:patient_id>/',views.patient_delete,name='patient_delete'),

  


] 