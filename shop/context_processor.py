def cart(request):
    cart = request.session.get('cart', {
        '1': {
            'price': 1000,
        }
    })

    return {
        'cart': list(cart.values()),
    }
