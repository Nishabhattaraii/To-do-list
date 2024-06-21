from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Your account has been created! You are now logged in as {user.username}')
            return redirect('todo-list')
    else:
        form = UserRegisterForm()
    return render(request, 'myapp/register.html', {'form': form})

def todo_list(request):
    return render(request, 'myapp/todo_list.html')
