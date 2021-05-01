import random
import string

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import SET_NULL
from django.utils.translation import ugettext_lazy as _


class ReferCode(models.Model):
    code = models.CharField(max_length=10, primary_key=True)


class UserManager(BaseUserManager):
    """
    Custom user model manager where to create user_refer_code.
    """

    def create_user(self, username, email, password, **extra_fields):

        email = self.normalize_email(email)  # todo: make case insensitive
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    used_refer_code = models.ForeignKey(ReferCode, null=True, blank=True, on_delete=SET_NULL, related_name='UserUsed')
    user_refer_code = models.OneToOneField(ReferCode, blank=True, on_delete=models.CASCADE, related_name='UserCreated')

    '''
    earned point can also be added here. but in this ,it is calculated by
    filtering user having used_refer_code = self.user_refer_code. as defined in view.UserViewSet point_earned.
    pros: one less row
    cons: 1> filtering user will take time,
          2> if referred user deleted, it will give less earned point then actual earned point.
    '''
    objects = UserManager()


def randCode():  # todo: efficient algo  to generate unique random sequential-pattern
    N = 10
    unique = False
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    while not unique:
        try:
            ReferCode.objects.get(code=res)

        except ReferCode.DoesNotExist:
            rcodeObj = ReferCode.objects.create(code=res)
            unique = True
            return rcodeObj

        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
