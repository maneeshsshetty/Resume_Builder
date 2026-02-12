from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('templates/', views.resume_templates, name='resume_templates'),
    path('templates/<int:resume_id>/', views.resume_templates, name='resume_templates'),
    path('create/', views.create_resume, name='create_resume'),
    path('resume/<int:resume_id>/download/<str:template_name>/', views.generate_pdf, name='generate_pdf'),
    path('resume/<int:resume_id>/view/', views.view_resume, name='view_resume'),
    path('search/', views.employee_search, name='employee_search'),
    path('about/', views.about, name='about'),
    path('employees/', views.employee_list, name='employee_list'),
    path('resume/<int:resume_id>/update/', views.update_resume, name='update_resume'),
    path('resume/<int:resume_id>/delete/', views.delete_resume, name='delete_resume'),
]
