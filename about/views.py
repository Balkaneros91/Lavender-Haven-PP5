from django.shortcuts import render
from .models import AboutUs, ThingsWeOffer


def about_view(request):
    """View returning the about page"""
    about_us = AboutUs.objects.last()
    things_we_offer = ThingsWeOffer.objects.all()

    context = {
        'about_us': about_us,
        'things_we_offer': things_we_offer
    }

    return render(request, 'about/about.html', context)
