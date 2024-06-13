from django import forms
from django.contrib.auth.models import User
from .models import Customer, Notification, Vehicle, ServiceRequest, Feedback

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['profile_pic', 'address', 'mobile']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['number', 'model']

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['vehicle', 'problem_description']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['mechanic', 'rating', 'feedback']


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['recipient', 'message',]
