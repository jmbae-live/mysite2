from django.urls import path, include
from account.views import CustomLoginView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
