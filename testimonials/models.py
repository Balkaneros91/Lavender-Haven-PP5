from django.db import models
from django.contrib.auth.models import User


class Testimonials(models.Model):
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    testimonial = models.TextField(max_length=1000, blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'testimonials'
        ordering = ['-created_on']
