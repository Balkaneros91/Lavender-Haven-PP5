from django.db import models


class AboutUs(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'about us'


class ThingsWeOffer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'things we offer'
