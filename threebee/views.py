from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        redirect('apicoltore', pk=request.user.apicoltore.pk)
    return render(request, 'threebee/index.html')


def logout_view(request):
    logout(request)
    return redirect('index')


class Login(LoginView):
    template_name = 'registration/login.html'


