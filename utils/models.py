from django.db import models

from utils.slugify import slugify_field


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_active = models.BooleanField(default=True, verbose_name='Активный?')

    class Meta:
        abstract = True


class SlugModel(BaseModel):
    name = models.CharField(max_length=255,
                            unique=True,
                            verbose_name='Название')
    slug = models.CharField(max_length=255,
                            unique=True,
                            blank=True, null=True,
                            editable=False,
                            verbose_name='Название в ссылке',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify_field(self.name, self)
        return super(SlugModel, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )

    class Meta:
        abstract = True
