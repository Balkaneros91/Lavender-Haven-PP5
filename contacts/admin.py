from django.contrib import admin
from .models import Contact, OpenHours


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone_number', 'address')


@admin.register(OpenHours)
class OpenHoursAdmin(admin.ModelAdmin):

    list_display = ('days', 'hours')
