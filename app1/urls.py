from django.urls import path

from . import views

app_name = "app1"

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('student/<int:student_id>', views.student, name='student'),
    path('Pending_Requests',views.Pending_Request, name='Pending_Request'),
    ]