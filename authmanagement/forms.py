from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth import get_user_model
User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]

# ********** start Change profile form ***************


# class EditForm(forms.ModelForm):
#     # email = forms.EmailField()
#     class Meta:
#         model = User
#         fields = ["first_name", "last_name", "email"]
