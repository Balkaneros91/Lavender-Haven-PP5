from django.contrib import admin
from .models import Contact, OpenHours, ContactMessage, Newsletter


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone_number', 'address')


@admin.register(OpenHours)
class OpenHoursAdmin(admin.ModelAdmin):

    list_display = ('days', 'hours')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email', 'created_on', 'message_subject')
    list_display = ('name', 'email', 'created_on', 'message_subject')
    search_fields = ('name', 'email', 'created_on', 'message_subject')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_filter = ('email', 'created_on')
    list_display = ('email', 'created_on')
    search_fields = ('email', 'created_on')
