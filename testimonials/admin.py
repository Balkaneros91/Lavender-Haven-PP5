from django.contrib import admin
from .models import Testimonials


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email', 'created_on', 'public')
    list_display = ('name', 'email', 'testimonial', 'created_on', 'public')
    search_fields = ('name', 'email', 'created_on', 'public')
    actions = ['approve_testimonial']

    def approve_testimonial(self, request, queryset):
        queryset.update(public=True)
