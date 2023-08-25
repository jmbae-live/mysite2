import base64

import requests
from celery import shared_task
from django.core.mail import send_mail

from mysite2 import settings
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
    # 토스 인증 - 시크릿 키를 base64 로 인코딩해서 헤더로 전달함
    encoding_str = (settings.TOSS_SECRET_KEY + ':').encode()
    encoded_secret_key = base64.urlsafe_b64encode(encoding_str)
    print(str(encoded_secret_key))
    # 결제 확인 API 호출
    toss_api_url = 'https://api.tosspayments.com/v1/payments/' + payment_key
    headers = {
        'Authorization': 'Basic ' + encoded_secret_key.decode('utf-8')
    }
    # 결과 확인 데이터베이스 업데이트
    response = requests.get(toss_api_url, headers=headers)
    res_data = dict(response.json())
    order_id = int(res_data['orderId'].replace('order-', ''))
    order = Order.objects.get(id=order_id)
    if res_data['status'] == 'DONE':
        order.paid = True
        order.save()
    else:
        print('status:' + res_data['status'])
    # print(dict(response.json()))
    return
