from django.urls import path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>', views.add_cart, name='add_cart'),
]
