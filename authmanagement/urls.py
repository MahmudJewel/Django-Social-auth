from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .views import RegisterView

urlpatterns = [
    path('signup', RegisterView.as_view(), name='signup'),
    path('login', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', LogoutView.as_view(
        template_name='auth/logout.html'), name='logout'),
    # reset pass
    path('password_reset', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_sent', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    # end pass reset

]
