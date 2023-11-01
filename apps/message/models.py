from django.db import models
from utils.models import SlugModel, BaseModel
from utils.choices import MessageTypeChoices, MessageStatusChoices
from apps.auth_user.models import CustomUser
from apps.chat.models import Group


class Messages(BaseModel):
    type = models.CharField(
        max_length=255,
        choices=MessageTypeChoices.choices,
        default=MessageTypeChoices.TEXT,
        null=True, blank=True,
        verbose_name='Тип сообщения')
    status = models.CharField(
        max_length=255,
        choices=MessageStatusChoices.choices,
        default=MessageStatusChoices.NEW,
        blank=True,
        verbose_name='Статус сообщения')
    context = models.TextField(
        verbose_name='Контекст сообщения')
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='message_owner',
        verbose_name='Владелец сообщения')
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='message_group',
        verbose_name='Группа сообщения')

    reply = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='reply_reply',
        verbose_name='Под сообщение',
        blank=True, null=True)

    class Meta:
        abstract = True


class TextMessage(Messages):
    context = models.CharField(
        max_length=1024,
        verbose_name='Контекст сообщения')

    def __str__(self):
        return f"{self.context[:50]}"

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.type = MessageTypeChoices.TEXT
        return super(TextMessage, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )

    class Meta:
        verbose_name = 'Текстовое сообщение'
        verbose_name_plural = 'Текстовые сообщения'
