from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from .forms import RegiseterForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages

# Create your views here.


def home(res):
    return render(res, "home.html")


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", {"user": request.user})
    else:
        return redirect('login')


def register(res):
    if not res.user.is_authenticated:
        if res.method == "POST":
            form = RegiseterForm(res.POST)
            messages.success(res, "Account create Successfuly ")
            if form.is_valid():
                form.save()
        else:
            form = RegiseterForm()
        return render(res, "register.html", {"form": form})
    else:
        return redirect('profile')


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            userpass = form.cleaned_data["password"]
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user , data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'passChange.html',{'form':form})
    else:
        return redirect('login')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user ,data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user = request.user)
        return render(request, 'passChange.html',{'form':form})
    else:
        return redirect('login')