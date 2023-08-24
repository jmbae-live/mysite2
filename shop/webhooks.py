from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def toss_webhook(request):
    payload = request.body
    print(str(payload))
    return HttpResponse(status=200)
