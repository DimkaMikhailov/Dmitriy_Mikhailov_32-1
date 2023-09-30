from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from users.forms import RegisterForm, LoginForm


def register_view(request):
    if request.method == 'GET':

        data = {'form': RegisterForm,
                'query': 'register'}
        return render(request, template_name='users/register_form.html', context=data)

    if request.method == 'POST':
        form_data = request.POST
        form = RegisterForm(form_data)
        if form.is_valid():
            if form.cleaned_data.get('password') == form.cleaned_data.get('confirm'):
                User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password'))
                return redirect(to='/users/login/')
            else:
                form.add_error('password', 'Try again!')

        data = {'form': form, 'query': 'register'}
        return render(request, template_name='users/register.html', context=data)


def login_view(request):
    if request.method == 'GET':
        data = {'form': LoginForm,
                'query': 'login'}
        return render(request, template_name='users/register_form.html', context=data)
    if request.method == 'POST':
        form_data = request.POST
        form = LoginForm(form_data)
        if form.is_valid():
            if user := authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            ):
                login(request=request, user=user)
                return redirect(to='/products/')
            else:
                form.add_error('password', 'Try agan!')
        data = {'form': form, 'query': 'login'}
        return render(request, template_name='users/register_form.html', context=data)


def logout_view(requests):
    logout(requests)
    return render(requests, template_name='products/index.html')
