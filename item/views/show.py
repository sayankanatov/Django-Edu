from django.shortcuts import render, get_object_or_404
from ..models import Item

# Create your views here.
def show(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    tags = ', '.join(item.title for item in item.tag.all())
    return render(request, 'item/show.html', locals())
