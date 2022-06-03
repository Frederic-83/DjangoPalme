from django.contrib.auth import login, authenticate, logout
from . import forms
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'blog/home.html')

def trombinoscope(request):
    return render(request, 'trombinoscope/trombinoscope.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            message = 'Identifiants invalides.'
    return render(request, 'adherent/login.html', context={'form': form, 'message': message})
