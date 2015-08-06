from django.contrib import admin

# Register your models here.

from .models import Event, Booth

admin.site.register(Event)
admin.site.register(Booth)
