from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),
    path('resume/', views.resume, name="resume"),
    path('contact/', views.contact, name="contact"),
    path('contact_request/', views.contact_request, name="contact_req")
]