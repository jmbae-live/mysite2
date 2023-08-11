from django.urls import path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>', views.add_cart, name='add_cart'),
    path('update/<int:product_id>', views.cart_update, name='update_cart'),
    path('remove/<int:product_id>', views.cart_remove, name='remove_cart'),

]
