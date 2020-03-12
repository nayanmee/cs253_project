from django.urls import path

from . import views

app_name = "myapp"

urlpatterns = [
    path('upload', views.upload,name='upload'),
    path('register', views.register, name='register'),
    path('login', views.login ,name='login'),
    #path('dashboard',views.dashboard,name='dashboard')
    #path('registration',views.regis,name='registration'),
]
