from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
# from django.http import HttpResponse
from django.contrib import messages

from articles.models import Article


def view_cart(request):
    """ A view to display the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the selected article to the shopping cart """

    article = get_object_or_404(Article, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {article.name} quantity to {cart[item_id]} in your cart')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {article.name} to your cart')

    request.session['cart'] = cart
    # print(request.session['cart'])
    return redirect(redirect_url)


def update_cart(request, item_id):
    """ Adjust the quantity of the selected article to the specified amount """

    article = get_object_or_404(Article, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {article.name} quantity to {cart[item_id]}')  # noqa
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {article.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_from_cart(request, item_id):
    """ Remove article from the shopping cart """

    try:
        article = get_object_or_404(Article, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(request, f'Removed {article.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing article: {e}')
        return HttpResponse(status=500)
