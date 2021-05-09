
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from hospital.views import index
from register.views import detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name = 'registration/login.html') ,name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'registration/logout.html'), name='logout'),
    path('detail/', detail_view, name='detail'),

]
