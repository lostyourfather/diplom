from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import os
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('user id'))
    group = models.CharField(max_length=10, null=False, blank=False, verbose_name=_('group'))
    phone_number = models.CharField(max_length=12, null=True, blank=True, verbose_name=_('phone number'))
    avatar = models.ImageField(upload_to='files/', blank=True, null=True, verbose_name=_('avatar'))

    class Meta:
        app_label = 'app_users'
        verbose_name_plural = _('profiles')
        verbose_name = _('profile')
