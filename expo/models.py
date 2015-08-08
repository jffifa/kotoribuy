# coding=utf-8
from django.db import models

# Create your models here.

class Event(models.Model):
    class Meta:
        verbose_name = u'展会'
        verbose_name_plural = u'展会'

    name = models.CharField(max_length=64, unique=True, verbose_name=u'名字')
    abbr = models.CharField(max_length=64, blank=True, default='', verbose_name=u'简写')

    def __unicode__(self):
        if self.abbr:
            return u'%s(%s)' % (self.name, self.abbr)
        else:
            return self.name

class Booth(models.Model):
    class Meta:
        verbose_name = u'摊位'
        verbose_name_plural = u'摊位'

    event = models.ForeignKey(Event, verbose_name=u'展会')
    circle = models.CharField(max_length=64, verbose_name=u'社团名/企业名')
    logo = models.ImageField(upload_to='booth-logo', blank=True, max_length=255, verbose_name=u'LOGO')
    location = models.CharField(max_length=64, blank=True, verbose_name=u'摊位号')
    page = models.URLField(max_length=255, blank=True, verbose_name=u'专门页面')
    tags = models.TextField(blank=True, verbose_name=u'标签（用英文逗号,分隔）')
    comment = models.TextField(blank=True, verbose_name=u'备注')
    tag_set = models.ManyToManyField(Tag, related_name='booth_set')

    def __unicode__(self):
        return u'%s - %s' % (self.circle, self.location)

class Tag(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name=u'tag名称')

    def __unicode__(self):
        return self.name