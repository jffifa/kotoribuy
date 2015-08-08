# coding=utf-8
import autocomplete_light
from .models import Tag


autocomplete_light.register(Tag,
    search_fields=['^name'],
    attrs={
        'data-autocomplete-minimum-characters':1,
    },
    widget_attrs={
        'data-widget-maximum-values':4,
    }
)
