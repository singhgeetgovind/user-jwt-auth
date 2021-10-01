from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(_('first name'), max_length=25)
    last_name = models.CharField(_('last name'), max_length=25)
    address = models.CharField(max_length=200,null=False,blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Token(models.Model):
    user = models.OneToOneField(CustomUser,blank=False,on_delete=models.CASCADE)
    token_key = models.CharField(max_length=150,default='')

    def __str__(self):
        return str(self.user)
    