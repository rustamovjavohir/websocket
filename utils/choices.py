from django.db.models import TextChoices


class UserRoleChoices(TextChoices):
    ADMIN = "admin", "Администратор"
    SUPER_ADMIN = "super_admin", "Супер администратор"
    OWNER = "owner", "Владелец"


class AuthStatusChoices(TextChoices):
    NEW = "new", "Новый"
    VERIFY = "verify", "На проверке"
    HALF_DONE = "half_done", "Частично заполнен"
    DONE = "done", "Заполнен"


class GroupTypeChoices(TextChoices):
    PUBLIC = "public", "Публичный"
    PRIVATE = "private", "Приватный"
    SUPER_GROUP = "super_group", "Супер группа"


class CurrencyChoices(TextChoices):
    USD = "USD", "Доллар"
    EUR = "EUR", "Евро"
    RUB = "RUB", "Рубль"
    UZS = "UZS", "Сум"


class MessageTypeChoices(TextChoices):
    TEXT = "text", "Текст"
    IMAGE = "image", "Изображение"
    VIDEO = "video", "Видео"
    FILE = "file", "Файл"


class MessageStatusChoices(TextChoices):
    NEW = "new", "Новый"
    READ = "read", "Прочитано"
    DELETED = "deleted", "Удалено"
