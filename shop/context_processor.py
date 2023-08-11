
def cart(request):
    cart = request.session.get('cart', {})

    return {
        'cart': cart,
    }
