#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.db import connection
from restful import restful
from ..forms import ImageForm
from django.urls import reverse

@restful
def add_image(request, item_id):
    form = ImageForm()
    return render(request, 'item/item_image.html',locals())

@add_image.method('POST')
def add_image(request, item_id):
    form = ImageForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'item/item_image.html',locals())
    data = b''
    for chunk in request.FILES['image'].chunks():
        data += chunk
    with connection.cursor() as cursor:
        cursor.execute('UPDATE item_item SET image = %s WHERE id = %s ;',
            [data, item_id]
        )
        return HttpResponseRedirect(reverse('item:index'))

def image(request, item_id):
    with connection.cursor() as cursor:
        cursor.execute('SELECT image FROM item_item WHERE id = %s ;',[item_id])
        (data, ) = cursor.fetchone()
    if not data:
        raise Http404()
    response = HttpResponse(content_type='image/jpeg')
    response.write(data)
    return response
