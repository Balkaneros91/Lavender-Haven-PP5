from django.db import models


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
