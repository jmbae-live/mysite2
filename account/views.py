from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


# Create your views here.
class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
