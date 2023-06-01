# from django.db import models
# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractUser

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError(_('Please enter an email address'))

#         email = self.normalize_email(email)

#         new_user = self.model(email=email, **extra_fields)

#         new_user.set_password(password)

#         new_user.save()

#         return new_user

#     def create_superuser(self, email, password, **extra_fields):

#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(_('Superuser must have is_superuser=True'))

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(_('Superuser must have is_staff=True'))

#         return self.create_user(email, password, **extra_fields)


# class User(AbstractUser):
#     email = models.CharField(_('Email'), max_length=80, unique=True)
#     date_joined = models.DateTimeField(_('Date'), auto_now_add=True)

#     REQUIRED_FIELDS = 'email'
#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return f"User {self.username}"

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
