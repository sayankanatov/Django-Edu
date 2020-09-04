#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from ..models import Item, Tag
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db import connection

def drop_tag(request, item_id, tag_id):
    with connection.cursor() as cursor:
        cursor.execute('DELETE FROM item_item_tag WHERE item_id = %s AND tag_id = %s;',[item_id, tag_id])
    return HttpResponseRedirect(reverse('item:tags', args=[item_id]))


def drop_tag_for_lamers(request, item_id, tag_id):
    item = get_object_or_404(Item, pk=item_id)
    tag = get_object_or_404(Tag, pk=tag_id)
    item.tag.remove(tag)
    item.save()
    return HttpResponseRedirect(reverse('item:tags', args=[item_id]))
