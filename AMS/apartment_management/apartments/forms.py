from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Apartment, Complaint, Payment

# Custom User Registration Form
class UserRegistrationForm(UserCreationForm):
    is_owner = forms.BooleanField(required=False, label="Register as Owner")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_owner']

# Apartment Form
class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'location', 'price', 'availability', 'image']

# Complaint Form
class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['subject', 'description']

# Payment Form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['apartment', 'amount']
