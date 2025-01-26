from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    pass


class Item(models.Model):
    name = models.CharField(_('Название'), 
                            max_length=100)
    cost = models.DecimalField(_('Цена'), max_digits=6, decimal_places=2)
    janer = models.CharField(_('Жанр игры'), max_length=100)
    description = models.TextField(_('Описание'))
    image = models.ImageField(_('Картинка'), upload_to='images/', blank=True, null=True, default='images/default.png')
    date = models.DateField(_('Дата выпуска'))

    class Meta:
        verbose_name = _('Предмет')
        verbose_name_plural = _('Предметы')
