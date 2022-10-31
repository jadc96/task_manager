from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import TaskCategoryForm, TaskForm, CustomUserCreationForm


def home(request):
    return render(request, 'base/home.html')

def register_page(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form, 'page': page}
    return render(request, 'base/login_register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email or password does not exists.')

    return render(request, 'base/login_register.html')

def logout_user(request):
    logout(request)
    return redirect('home')
