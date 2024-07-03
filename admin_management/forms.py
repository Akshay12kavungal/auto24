from django import forms

from admin_management.models import Booking, RentalCar


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RentalCarForm(forms.ModelForm):
    class Meta:
        model = RentalCar
        fields = ['name', 'description', 'image', 'daily_rate', 'availability']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'start_date', 'end_date']