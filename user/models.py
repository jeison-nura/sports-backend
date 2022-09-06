from collections import UserDict
from enum import Enum
from multiprocessing.sharedctypes import Value
from typing import OrderedDict

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    email = models.EmailField(unique=True)

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The username must not be empty')

        if not email:
            raise ValueError('The email must be valie and different than empty')
        
        if not password:
            raise ValueError('The password should not be empty')
    
        return User.objects.create(username, email, password, **extra_fields)

    def create_user(self, username: str, email: str, password: str, **extra_fields):
        """"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_super_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)

class Genders(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Profile(models.Model):
    GENDER_CHOICES = (
        ('MALE', Genders.MALE),
        ('FEMALE', Genders.FEMALE),
        ('OTHER', Genders.OTHER),
    )
    nickname = models.CharField(max_length=1000)
    gender = models.CharField(choices=GENDER_CHOICES, null=False, default=Genders.OTHER, max_length=20)
    avatar_url = models.URLField(null=True)
    description = models.CharField(max_length=1000)
    size = models.FloatField()
    weight = models.IntegerField()
    birth_date = models.DateField()
    location = models.CharField(max_length=500)
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE
    )




