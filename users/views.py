from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} ! Your account has been created! You are now able to log in.')
            return redirect('login')

    else:
        form = UserRegisterForm()

    context ={
        'form': form,
        'title': 'Register'
    }    
    return render(request, 'users/register.html', context)


def profile(request):
    return render(request, 'users/profile.html')
