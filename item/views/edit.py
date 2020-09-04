from django.shortcuts import render, get_object_or_404
from ..models import Item
from ..forms import ItemModelForm
import sys
from restful import restful
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@restful
def edit(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = ItemModelForm(instance=item)
    return render(request, 'item/edit.html', locals())

@edit.method('POST')
def update(request, item_id):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('item:index'))
    if not request.user.is_superuser:
        if not request.user.has_perm('item.change_item'):
            return HttpResponseRedirect(reverse('item:index'))
    raw_data = dict()
    raw_data.update(request.POST)
    item = get_object_or_404(Item, pk=item_id)

    form = ItemModelForm(request.POST, instance=item)
    if form.is_valid():
        item.save()
        return render(request, 'item/show.html', locals())
    else:
        return render(request, 'item/edit.html', locals())
