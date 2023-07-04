from django.db import models
import uuid


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class OpenHours(models.Model):
    days = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'open hour'
        verbose_name_plural = 'open hours'


class ContactMessage(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(max_length=500, blank=False, null=True)
    message_subject = models.CharField(
        'subject', max_length=50, blank=False, null=True)
    message = models.TextField(max_length=1000, blank=False, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=500, blank=False, null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.email)
