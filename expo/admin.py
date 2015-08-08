from django.contrib import admin

# Register your models here.

from .models import Event, Booth, Tag

admin.site.register(Event)
admin.site.register(Booth)
admin.site.register(Tag)