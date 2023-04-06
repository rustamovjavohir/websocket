from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='user_photo', verbose_name="Фото", null=True, blank=True)
    channel_name = models.CharField(max_length=100, verbose_name="Название канала", null=True, blank=True)
    is_online = models.BooleanField(default=False, verbose_name="Онлайн")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
