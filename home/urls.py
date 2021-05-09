from django.urls import path
from home import views 

# Django Olny looks at Main Url.py


urlpatterns = [
   path('',views.home,name='home'),
] 