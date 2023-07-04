from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('', views.testimonials, name='testimonials'),
    path('add/', views.add_testimonial, name='add_testimonial'),
]
