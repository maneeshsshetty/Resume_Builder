from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('templates/', views.resume_templates, name='resume_templates'),
    path('templates/<int:resume_id>/', views.resume_templates, name='resume_templates'),
    path('create/', views.create_resume, name='create_resume'),
    path('resume/<int:resume_id>/download/<str:template_name>/', views.generate_pdf, name='generate_pdf'),
    path('about/', views.about, name='about'),
]
