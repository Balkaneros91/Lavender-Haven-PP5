from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm
from .models import Contact, OpenHours, ContactMessage


def contacts_view(request):
    """
    View returning the contacts page and handling contact message submission.
    """
    contacts = Contact.objects.first()
    open_hours = OpenHours.objects.all()

    redirect_url = '/'  # Default value for redirect_url

    if request.method == 'POST':
        try:
            redirect_url = request.POST.get('redirect_url', '/')
            name = request.POST['name']
            email = request.POST['email']
            message_subject = request.POST['message_subject']
            message = request.POST['message']
            form = ContactMessageForm(request.POST)
            if form.is_valid():
                new_message = form.save(commit=False)
                new_message.name = name
                new_message.email = email
                new_message.message_subject = message_subject
                new_message.message = message
                new_message.save()
                messages.success(request, "Message sent!")
                return redirect(redirect_url)
            else:
                messages.error(
                    request, "Please make sure to fill out all the fields.")
        except ValueError:
            messages.error(
                request, "Please make sure to fill out your details before \
                        leaving a message.")
            return redirect(redirect_url)

    context = {
        'contacts': contacts,
        'open_hours': open_hours,
        # Create a new form instance to render in the template
        'contact_form': ContactMessageForm()
    }

    return render(request, 'contacts/contacts.html', context)
