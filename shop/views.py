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


def cart_detail(request):
    return render(request, 'cart/detail.html', {})
