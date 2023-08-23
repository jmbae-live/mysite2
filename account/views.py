from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import MyLoginForm, MyRegisterForm


# Create your views here.
class CustomLoginView(LoginView):
    form_class = MyLoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    form_class = MyRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
