from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='user_photo', verbose_name="Фото", null=True, blank=True)
    salom = models.CharField(max_length=100, verbose_name="Салом", null=True, blank=True)
