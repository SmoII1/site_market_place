from django.http import HttpResponse
from django.shortcuts import render
from market_place import models
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def items(request):
    items_spisok = models.Item.objects.all()
    a = render(request, 'main.html', context={'items_spisok': items_spisok})
    return a


def item_card(request, item_name):
    try:
        item = models.Item.objects.get(name=item_name)
        a = render(request, 'item_card.html', context={'product': item})
        return a
    except models.Item.DoesNotExist:
        b = render(request, '404.html')
        return b


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def cart(request):
    return HttpResponse("<h1>Эта страница ещё не готова, она появится позже.</h1>")


def profile_user(request, user_id):
    return HttpResponse("<h1>Эта страница ещё не готова, она появится позже.</h1>")


def log_in(request):
    if request.method == "GET":
        a = render(request, 'login.html')
        return a
    else:
        user = request.POST['username']
        password = request.POST['user_password']
        a = authenticate(request, username=user, password=password)
        if a != None:
            login(request, a)
            b = redirect('main')
            return b
        else:
            b = render(request, 'login.html')
            return b


def log_out(request):
    logout(request)
    return redirect('main')
