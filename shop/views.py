from decimal import Decimal

from django.shortcuts import render, redirect, get_object_or_404

from shop.models import Product


# Create your views here.
def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # 세션 'cart' 정보 가져오기
    cart = request.session.get('cart', {})
    cart[str(product_id)] = {
        'quantity': 1,
        'price': str(product.price),
    }
    # cart 변수를 세션에 저장
    request.session['cart'] = cart
    request.session.modified = True

    return redirect('shop:cart_detail')


def cart_remove(request, product_id):
    cart = request.session.get('cart', {})
    del cart[str(product_id)]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('shop:cart_detail')


def cart_update(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)]['quantity'] = Decimal(request.POST.get('quantity'))
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('shop:cart_detail')


def cart_detail(request):
    cart = request.session.get('cart', {})
    product_ids = cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    for product in products:
        cart[str(product.id)]['product'] = product
    for key, item in cart.items():
        item['price'] = Decimal(item['price'])
        item['total_price'] = item['price'] * item['quantity']
        cart[key] = item
    total_price = sum(Decimal(item['price']) * item['quantity'] for item in cart.values())

    return render(request, 'cart/detail.html', {
        'cart_dict': cart,
        'total_price': total_price
    })


def order_create(request):
    return render(request, 'shop/order_created.html', {})
