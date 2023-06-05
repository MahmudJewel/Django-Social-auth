from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordResetView
from .forms import RegisterForm

class RegisterView(CreateView):
    template_name = 'auth/signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

class CustomPasswordResetView(PasswordResetView):
    template_name = 'auth/password_reset.html'
    email_template_name = 'auth/password_reset_notification.html'
    success_url = '/'
