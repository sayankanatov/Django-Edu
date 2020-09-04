from django.shortcuts import render
from django.template import loader
from ..models import Item
from django.http import HttpResponse
# Create your views here.


def index(request):
    fmt = request.GET.get('format','html').lower()
    if fmt == 'xml':
        template_name = 'item/index.xml'
        resp_type = 'text/xml; charset=utf-8'
    elif fmt == 'json':
        template_name = 'item/index.json'
        resp_type = 'text/json; charset=utf-8'
    else:
        template_name = 'item/index.html'
        resp_type = 'text/html; charset=utf-8'

    items = Item.objects.all()
    template = loader.get_template(template_name)
    text = template.render(locals(), request)
    return HttpResponse(text, content_type=resp_type)
