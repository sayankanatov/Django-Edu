from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from ..models import Item
# Create your views here.
def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse("item:index"))

