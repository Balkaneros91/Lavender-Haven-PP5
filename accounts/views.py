from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserAccount
from .forms import UserAccountForm

from checkout.models import Order


@login_required
def account(request):
    """ Display the user's account. """
    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')   # noqa
    else:
        form = UserAccountForm(instance=account)
    orders = account.orders.all()

    template = 'accounts/account.html'
    context = {
        'form': form,
        'orders': orders,
        'on_account_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_account': True,
    }

    return render(request, template, context)
