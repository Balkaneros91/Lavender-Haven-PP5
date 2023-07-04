from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

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


@login_required(login_url='account_login')
def edit_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonials, pk=pk)

    # Check if the logged-in user is the owner of the booking
    if testimonial.email != request.user.email:
        return HttpResponseForbidden("You don't have permission to access this testimonial.")

    if request.method == 'POST':
        form = TestimonialsForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial successfully updated!')
            return redirect('testimonials')
    else:
        form = TestimonialsForm(instance=testimonial)
    context = {'form': form}
    return render(request, 'testimonials/edit_testimonial.html', context)
