from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm
from django.contrib.auth.decorators import login_required



@login_required
def dashboard_view(request):
    return render(request, "users/dashboard.html")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  
    else:
        form = SignupForm()
    return render(request, "users/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
