from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import *
from .forms import *

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Usuario o contraseña incorrectos')   
    context = {}
    return render(request, 'accounts/login.html', context)

def register(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Cuenta creada')
                return redirect('login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def logout(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'accounts/home.html', context)