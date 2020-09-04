#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from ..models import Item, Tag
from ..forms import TagListForm
from restful import restful
from django.db import connection
from textwrap import dedent
from django.http import HttpResponseRedirect


@restful
def tags(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = TagListForm()
    return render(request, 'item/tags.html',locals())


@tags.method('post')
def tags(request, item_id):
    form = TagListForm(request.POST)
    if form.is_valid():
        tag_list = form.cleaned_data['tag_list']
        tag_list = tag_list.split(',')
        tag_list = map(str.strip, tag_list)
        tag_list = map(str.lower, tag_list)
        with connection.cursor() as cursor:
            for tag in tag_list:
                cursor.execute(dedent('''\
                    INSERT INTO item_tag (title) 
                    VALUES (%s)
                    ON CONFLICT DO NOTHING;'''),[tag])
                new_tag = get_object_or_404(Tag, title=tag)
                cursor.execute(dedent('''\
                    INSERT INTO item_item_tag (item_id, tag_id)
                    VALUES (%s, %s)
                    ON CONFLICT DO NOTHING;'''),
                    [item_id, new_tag.id])
                    # [item_id, tag])
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item/tags.html',locals())
