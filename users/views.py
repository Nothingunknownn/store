from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.urls import reverse

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


@login_required()
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, template_name='users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Регистрация прошла успешно!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, template_name='users/registration.html', context=context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    context = {
        'title': 'Store - Профиль',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, template_name='users/profile.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))