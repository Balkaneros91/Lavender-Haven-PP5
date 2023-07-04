from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Testimonials
from .forms import TestimonialsForm


def testimonials(request):
    """ A view to return the testimonials page """

    if request.user.is_superuser:
        testimonials = Testimonials.objects.all()
    else:
        # testimonials = Testimonials.objects.filter(user=request.user)
        testimonials = Testimonials.objects.filter(public=True)

    context = {'testimonials': testimonials}

    return render(request, 'testimonials/testimonials.html', context)


@login_required(login_url='account_login')
def add_testimonial(request):
    testimonial_form = TestimonialsForm()

    if request.method == 'POST':
        testimonial_form = TestimonialsForm(request.POST)
        if testimonial_form.is_valid():
            testimonial = testimonial_form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Your testimonial awaits for approval.')
            return redirect('testimonials')

    context = {'form': testimonial_form}
    return render(request, 'testimonials/add_testimonial.html', context)
