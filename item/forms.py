#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms
from .models import Item


class ItemForm(forms.Form):
    title = forms.CharField(label='Title', max_length=256)
    article = forms.CharField(label='Article', max_length=16)
    quantity = forms.IntegerField(label='Quantity', min_value=0)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)


class ItemModelForm(forms.ModelForm):

    # Тут создается сама форма если это надо
    class Meta:
        model = Item
        fields = ['title', 'article', 'quantity', 'description']


class TagListForm(forms.Form):
    tag_list = forms.CharField(label='New', required=False)


class ImageForm(forms.Form):
    image = forms.FileField(label="Image")

