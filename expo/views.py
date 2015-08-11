from django.shortcuts import render
from expo.models import Tag, Booth


# Create your views here.
def index(request):
    return tag_filter(request)

def booth_detail(request, booth_id=None):
    context = {}

    booth = Booth.objects.get(pk=booth_id)
    booth_tags = booth.tag_set.all()

    context['booth'] = booth
    context['booth_tag'] = booth_tags

    return render(request, 'expo/booth_detail.html', context)


def tag_filter(request, tag_id=None, tag_query=''):
    if tag_id:
        tag_id = int(tag_id)

    context = {}

    if tag_query:
        tags = Tag.objects.filter(name__contains=tag_query)
        context['tag_query'] = tag_query
    elif tag_id:
        tags = Tag.objects.filter(id=tag_id)
        context['tag_query'] = tags[0].name
    else:
        tags = Tag.objects.all()

    tags = tags.order_by('name')
    context['tags'] = tags

    if tag_query or tag_id:
        booth_map = {}
        for tag in tags:
            for b in tag.booth_set.all():
                if b.id not in booth_map:
                    booth_map[b.id] = b

        booths = booth_map.values()
    else:
        booths = Booth.objects.all()

    context['booths'] = booths

    return render(request, 'expo/tag_booth_list.html', context)

