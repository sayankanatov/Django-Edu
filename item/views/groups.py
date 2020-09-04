from django.shortcuts import render
from ..models import Group

# Create your views here.

def groups(request):
    groups = Group.objects.all()
    return render(request, 'group/index.html', locals())
