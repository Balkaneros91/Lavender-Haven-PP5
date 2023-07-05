from django.contrib import admin
from . import views
from django.urls import path


urlpatterns = [
    path('', views.testimonials, name='testimonials'),
    path('detail/<int:pk>/', views.testimonial_detail, name='testimonial_detail'),
    path('add/', views.add_testimonial, name='add_testimonial'),
    path('edit/<int:pk>/', views.edit_testimonial, name='edit_testimonial'),
    path('delete/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
]
