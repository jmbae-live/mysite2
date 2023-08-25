from celery import shared_task
from django.core.mail import send_mail

from shop.models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"주문번호: {order.id}"
    message = f"안녕하세요 {order.name}님, \n\n" \
              f"주문을 완료했습니다." \
              f"주문번호는 {order.id} 입니다."
    mail_sent = send_mail(subject, message, 'admin@example.com', [order.email])
    print(message)
    return mail_sent


@shared_task
def toss_payment_confirm(payment_key, order_id):
    print('toss_payment_confirm:' + payment_key)
    # 토스 인증
    # 결제 확인 API 호출
    # 결과 확인 데이터베이스 업데이트
    return
