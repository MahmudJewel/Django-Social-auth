from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm


class RegisterView(CreateView):
    template_name = 'auth/signup.html'
    form_class = RegisterForm
    success_url = reverse_lazy('/')


# class RegisterView():
#     def post():
#         register_form = RegisterForm()

# def createUser(request):
#     template_name = 'auth/signup.html'
#     register_form = RegisterForm()
#     context = {
#         'register_form': register_form,
#     }
#     return render(request, template_name, context)


