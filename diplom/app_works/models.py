from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Work(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('title'))
    description = models.TextField(null=False, blank=False, verbose_name=_('description'))

    class Meta:
        app_label = 'app_works'
        verbose_name_plural = _('works')
        verbose_name = _('work')


class WorkUser(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'app_works'
        verbose_name_plural = _('works for user')
        verbose_name = _('work for user')


class Image(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='files/works-images/', blank=True, null=True)

    class Meta:
        app_label = 'app_works'
        verbose_name_plural = _('images')
        verbose_name = _('image')


class File(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name=_('title'))
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='files/works-files/', blank=True, null=True)

    class Meta:
        app_label = 'app_works'
        verbose_name_plural = _('files')
        verbose_name = _('file')


class Solution(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')
