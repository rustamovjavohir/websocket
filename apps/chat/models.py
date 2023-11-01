from django.db import models
from apps.auth_user.models import CustomUser
from utils.choices import GroupTypeChoices
from utils.models import SlugModel, BaseModel


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название комнаты")
    online = models.ManyToManyField(CustomUser, related_name='rooms', blank=True, verbose_name="Пользователи")

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'


class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Комната")
    content = models.CharField(max_length=512, verbose_name="Сообщение")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]} [{self.timestamp.strftime("%d.%m.%Y %H:%M")}]'


class Group(SlugModel):
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='groups_owner',
        verbose_name='Владелец группы')
    type = models.CharField(
        max_length=255,
        choices=GroupTypeChoices.choices,
        default=GroupTypeChoices.PUBLIC,
        blank=True,
        verbose_name='Тип группы')
    members = models.ManyToManyField(
        CustomUser,
        related_name='groups_members',
        verbose_name='Пользователи',
        blank=True)

    def generate_group_link(self):
        return f'/group/{self.slug}'

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
