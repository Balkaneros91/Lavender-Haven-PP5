from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts_view, name='contacts'),
    path('newletter/', views.newsletter, name='newsletter'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
]
