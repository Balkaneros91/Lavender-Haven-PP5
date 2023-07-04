from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactMessageForm, UpdateNewsletter
from .models import Contact, OpenHours, ContactMessage, Newsletter


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


def newsletter(request):
    """
    Allows user to sign up for a newsletter,
    Checks if the email is already in the database,
    Aborts process and informs user if so.
    """
    try:
        if request.method == 'POST':
            email = request.POST['email']
            redirect_url = request.POST['redirect_url']
            already_signed_up = Newsletter.objects.values_list(
                'email', flat=True)

            if email in already_signed_up:
                messages.error(
                    request, "This email address is already signed up!")
            else:
                form = UpdateNewsletter(request.POST)
                newsletter = form.save(commit=False)
                newsletter.email = email
                newsletter.save()
                messages.success(
                    request,
                    f"{email} has been successfully added to our mailing list")
            return redirect(redirect_url)
    except ValueError:
        messages.error(
            request, "Please enter valid Email address....")
        return redirect(redirect_url)


def unsubscribe(request):
    try:
        subscribed = Newsletter.objects.values_list('email', flat=True)

        if request.method == 'POST':
            email = request.POST['email']
            if email in subscribed:
                to_remove = Newsletter.objects.get(email=email)
                to_remove.delete()
                messages.success(
                    request,
                    f"{email} has been removed from our mailing list."
                )
            else:
                messages.error(
                    request,
                    "Sorry we couldn't find that email on our mailing list.")
            return redirect('home')
    except Exception:
        messages.error(
            request, 'Whoops, Houston we have a problem!'
        )
        return redirect('home')
    return render(request, 'contacts/unsubscribe.html')
