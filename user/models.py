from enum import Enum

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    email = models.EmailField(unique=True)

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




