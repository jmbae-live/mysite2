from django.urls import path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/', views.add_cart, name='add_cart'),
    path('update/<int:product_id>', views.cart_update, name='update_cart'),
    path('remove/<int:product_id>', views.cart_remove, name='remove_cart'),
    path('order_create/', views.order_create, name='order_create'),
    path('success/', views.payment_success, name='payment_success'),
    path('fail/', views.payment_fail, name='payment_success'),
    path('payment_test/<int:order_id>/', views.payment_test, name='payment_test'),  # 결제 테스트용 임시 페이지
]
