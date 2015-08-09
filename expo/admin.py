from django.contrib import admin

# Register your models here.

import autocomplete_light
from .models import Event, Booth, Tag, BoothTag


class BoothTagInline(admin.StackedInline):
    form = autocomplete_light.modelform_factory(BoothTag, exclude=[])
    model = BoothTag
    extra = 0


class BoothAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(Booth, exclude=[])

    inlines = [BoothTagInline,]

    search_fields = ['circle', 'location', 'tag']

admin.site.register(Event)
admin.site.register(Booth, BoothAdmin)
admin.site.register(Tag)
