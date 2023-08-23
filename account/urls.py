from django.urls import path, include

from .views import RegisterView, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
]
