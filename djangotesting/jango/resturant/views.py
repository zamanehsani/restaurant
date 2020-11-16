from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from resturant.forms import UserRegisterForm, UserUpdateForm, UserProfileUpdateForm
from resturant.models import Profile

def base(request):
    return render(request, 'base.html')

def table(request):
    return render(request, 'table.html')

def basefinal(request):
    return render(request, 'basefinal.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def profile(request):
    if request.method == "POST":
        u_from = UserUpdateForm(request.POST,  instance= request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_from.is_valid() and p_form.is_valid():
            u_from.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_from = UserUpdateForm(instance= request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

    context ={
        'u_form': u_from,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)


def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {uname}!')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    context ={'form':form }
    return render(request, 'register.html', context)