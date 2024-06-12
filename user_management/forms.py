from django import forms
from django.contrib.auth.models import User
from .models import Customer, Mechanic, ServiceRequest, Feedback, Vehicle
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['profile_pic', 'address', 'mobile']

class MechanicForm(forms.ModelForm):
    class Meta:
        model = Mechanic
        fields = ['profile_pic', 'address', 'mobile', 'skill', 'salary']

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['vehicle', 'problem_description']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['number', 'model', 'customer']  # Add 'customer_name' field to the form

    

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)