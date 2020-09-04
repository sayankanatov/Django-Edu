from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import LoginForm
from django.utils.http import is_safe_url, urlunquote

# Create your views here.


def index_full(request):
    current_time = datetime.now()
    context = {
        'current_time': current_time
    }
    template = loader.get_template('home/index.html')
    text = template.render(context, request)
    return HttpResponse(text)


def index(request):
    return render(request, 'generic.html', locals())


def user_login(request):
    # Вход в систему
    form = LoginForm(request.POST)
    if form.is_valid():
        s_login = str(form.cleaned_data['login'])
        password = str(form.cleaned_data['password'])
        user = authenticate(request, username=s_login, password=password)
        if user is not None:
            login(request, user)
    # Ступай откуда пришел
    way = request.META.get('HTTP_REFERER')
    if way:
        way = urlunquote(way)
    if not is_safe_url( url=way, allowed_hosts=request.get_host()):
        way = reverse('home:index')
    return HttpResponseRedirect(way)


def user_logout(request):
    logout(request)
    # request.session['my-cookie'] = 'Successfully logout'
    return HttpResponseRedirect(reverse('home:index'))
