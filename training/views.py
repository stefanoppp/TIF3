from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def home(request):
    return render(request,"training/home.html")

@login_required
def train(request):
    return render(request,"training/train.html")

@login_required
def developer_mode(request):
    return render(request, "training/developer_mode.html")

@login_required
def automatic_mode(request):
    return render(request, "training/automatic_mode.html")

def exit(request):
    logout(request)
    return redirect(home)