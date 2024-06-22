from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = 'home'

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class RegisterView(View):
    form_class = CustomUserCrationForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})
