from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from admin_management.forms import LoginForm
from .models import Customer, Vehicle, ServiceRequest, Feedback
from .forms import UserForm, CustomerForm, VehicleForm, ServiceRequestForm, FeedbackForm
from mechanic_management.models import Mechanic

def signup_customer(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST, request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('login_customer')
    else:
        user_form = UserForm()
        customer_form = CustomerForm()
    return render(request, 'registrations/signup_customer.html', {'user_form': user_form, 'customer_form': customer_form})

def login_customer(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and hasattr(user, 'customer'):
                login(request, user)
                return redirect('customer_home')
            else:
                return render(request, 'registrations/login_customer.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registrations/login_customer.html', {'form': form})

login_required
def customer_home(request):
    customer = Customer.objects.get(user=request.user)
    service_requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'customer/customer_home.html', {'service_requests': service_requests})

@login_required
def fill_vehicle_details(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.customer = Customer.objects.get(user=request.user)
            vehicle.save()
            return redirect('make_service_request')
    else:
        form = VehicleForm()
    return render(request, 'customer/fill_vehicle_details.html', {'form': form})


@login_required
def make_service_request(request):
    if request.method == 'POST':
        service_request_form = ServiceRequestForm(request.POST)
        if service_request_form.is_valid():
            service_request = service_request_form.save(commit=False)
            service_request.customer = Customer.objects.get(user=request.user)
            vehicle = Customer.objects.get(user=request.user).vehicles.last()
            service_request.vehicle = vehicle
            service_request.save()
            return redirect('customer_home')  # Redirect to customer's home page after submitting the service request
    else:
        service_request_form = ServiceRequestForm()
    return render(request, 'customer/make_service_request.html', {'form': service_request_form})

@login_required
def delete_service_request(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk, customer__user=request.user)
    if service_request.status == 'Pending':
        service_request.delete()
    return redirect('customer_home')

@login_required
def customer_profile(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_home')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/customer_profile.html', {'form': form})
@login_required
def customer_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.customer = Customer.objects.get(user=request.user)
            feedback.save()
            return redirect('customer_home')
    else:
        form = FeedbackForm()
    return render(request, 'customer/customer_feedback.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')  