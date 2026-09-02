from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, ApartmentForm, ComplaintForm, PaymentForm
from .models import Apartment, Complaint, Payment

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")  # ✅ Use .get() to avoid KeyError
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("home")  # Redirect to home page
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Please enter both username and password")

    return render(request, "login.html")


# User Logout View
def user_logout(request):
    logout(request)
    return redirect('login')
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')  # Redirects to login page if not logged in
def home(request):
    apartments = Apartment.objects.filter(availability=True)  # Show available apartments
    return render(request, 'home.html', {'apartments': apartments})

# Complaint Submission View
def submit_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('home')
    else:
        form = ComplaintForm()
    return render(request, 'complaint.html', {'form': form})

# Payment Processing View
def make_payment(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('home')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})


from django.shortcuts import render
from .models import Apartment

def user_dashboard(request):
    apartments = Apartment.objects.filter(availability=True)  # Show only available apartments
    return render(request, 'user_dashboard.html', {'apartments': apartments})
