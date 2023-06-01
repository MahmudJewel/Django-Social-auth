from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView

urlpatterns = [
    path('signup', RegisterView.as_view(), name='signup'),
    path('login', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', LogoutView.as_view(
        template_name='auth/logout.html'), name='logout'),
]
