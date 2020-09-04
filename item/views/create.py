from django.shortcuts import render
from ..models import Item
from ..forms import ItemModelForm
from restful import restful
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@restful
def create(request):
    item = Item()
    form = ItemModelForm(instance=item)
    return render(request, 'item/edit.html',locals())

@create.method('POST')
def create(request):
    item = Item()
    form = ItemModelForm(request.POST, instance=item)
    if form.is_valid():
        item.save()
        return HttpResponseRedirect(reverse('item:show_item', args=[item.pk]))


