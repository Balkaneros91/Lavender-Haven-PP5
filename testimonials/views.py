from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import Testimonials


def testimonials(request):
    """ A view to return the testimonials page """

    if request.user.is_superuser:
        testimonials = Testimonials.objects.all()
    else:
        # testimonials = Testimonials.objects.filter(user=request.user)
        testimonials = Testimonials.objects.filter(public=True)

    context = {'testimonials': testimonials}

    return render(request, 'testimonials/testimonials.html', context)
