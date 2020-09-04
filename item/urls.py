#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:item_id>/', views.show, name='show_item'),
    path('edit/<int:item_id>/', views.edit, name='edit_item'),
    path('delete/<int:item_id>/', views.delete, name='delete_item'),
    path('create/', views.create, name='create_item'),
    path('group/', views.groups, name='groups'),
    path('tags/<int:item_id>/', views.tags, name='tags'),
    path('tags/<int:item_id>/remove_tag/<int:tag_id>/', views.drop_tag, name='drop_tag'),
    path('add_image/<int:item_id>/', views.add_image, name='add_image'),
    path('image/<int:item_id>/', views.image, name='image'),
    path('graph/', views.graph, name="graph")
]
