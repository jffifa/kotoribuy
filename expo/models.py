# coding=utf-8
from __future__ import unicode_literals, absolute_import
from django.db import models

# Create your models here.

class Event(models.Model):
    class Meta:
        verbose_name = '展会'
        verbose_name_plural = '展会'

    name = models.CharField(max_length=64, unique=True, verbose_name='名字')
    abbr = models.CharField(max_length=64, blank=True, default='', verbose_name='简写')

    def __unicode__(self):
        if self.abbr:
            return '%s(%s)' % (self.name, self.abbr)
        else:
            return self.name


class Tag(models.Model):

    name = models.CharField(max_length=255, blank=False, null=False, unique=True, verbose_name='tag名称')

    def __unicode__(self):
        return self.name


class Booth(models.Model):
    class Meta:
        verbose_name = '摊位'
        verbose_name_plural = '摊位'

    event = models.ForeignKey(Event, verbose_name='展会')
    circle = models.CharField(max_length=64, verbose_name='社团名/企业名')
    logo = models.ImageField(upload_to='booth-logo', blank=True, max_length=255, verbose_name='LOGO')
    location = models.CharField(max_length=64, blank=True, verbose_name='摊位号')
    page = models.URLField(max_length=255, blank=True, verbose_name='特设页面')
    tags = models.TextField(blank=True, verbose_name='标签（用英文逗号,分隔）')
    comment = models.TextField(blank=True, verbose_name='备注')
    tag_set = models.ManyToManyField(Tag, through='BoothTag', through_fields=('booth','tag'), related_name='booth_set')

    def __unicode__(self):
        return '%s - %s' % (self.circle, self.location)

    def save(self, *args, **kwargs):
        def parse_tags(tag_str):
            sp = ','
            tags = [t.strip() for t in tag_str.strip().split(sp)]
            tags = [t for t in tags if t]
            return tags

        super(Booth, self).save(*args, **kwargs)

        tags = parse_tags(self.tags)
        # synchronize booth tag relationship
        for t in self.tag_set.all():
            if not t.name in tags:
                BoothTag.objects.filter(booth=self, tag=t).delete()

        for t in tags:
            tag, created = Tag.objects.get_or_create(name=t)
            if not BoothTag.objects.filter(booth=self, tag=tag).exists():
                BoothTag.objects.create(booth=self, tag=tag)


class BoothTag(models.Model):
    class Meta:
        db_table = 'expo_booth_tag_set'

    booth = models.ForeignKey(Booth)
    tag = models.ForeignKey(Tag)
