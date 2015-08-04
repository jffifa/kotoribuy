from django.db import models

# Create your models here.

class Event(models.Model):
    class Meta:
        verbose_name = u'展会'
        verbose_name_plural = u'展会'

    name = models.CharField(max_length=64, unique=True, verbose_name=u'名字')
    abbr = models.CharField(max_length=64, blank=True, default='', verbose_name=u'简写')

class Booth(models.Model):
    class Meta:
        verbose_name = u'摊位'
        verbose_name_plural = u'摊位'

    circle = models.CharField(max_length=64, verbose_name=u'')
