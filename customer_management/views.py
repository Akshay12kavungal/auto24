from pyexpat.errors import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from admin_management.forms import BookingForm, LoginForm, RentalCarForm
from admin_management.models import Booking, RentalCar
from .models import Customer, Notification, Vehicle, ServiceRequest, Feedback
from .forms import UserForm, CustomerForm, VehicleForm, ServiceRequestForm, FeedbackForm
from mechanic_management.models import Mechanic, MechanicWork

def signup_customer(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST, request.FILES)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
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




@login_required
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
def service_request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, customer__user=request.user)
    mechanic_work = MechanicWork.objects.filter(service_request=service_request).first()
    return render(request, 'customer/service_request_detail.html', {'service_request': service_request, 'mechanic_work': mechanic_work})



    
   

@login_required
def view_customer_profile(request):
    customer = Customer.objects.get(user=request.user)
    return render(request, 'customer/customer_profile.html', {'customer': customer})

@login_required
def update_customer_profile(request):
    customer = Customer.objects.get(user=request.user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('view_customer_profile')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/update_customer_profile.html', {'form': form})


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


@login_required
def notification_list(request):
    notifications = request.user.notifications.filter(is_read=False)
    return render(request, 'customer/notification_list.html', {'notifications': notifications})

@login_required
def booking_history(request):
    customer = Customer.objects.get(user=request.user)
    service_requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'customer/booking_history.html', {'service_requests': service_requests})


def rental_car_list(request):
    rental_cars = RentalCar.objects.all()
    return render(request, 'customer/rental_cars/rental_car_list.html', {'rental_cars': rental_cars})


def book_car(request, car_id):
    rental_car = RentalCar.objects.get(pk=car_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.rental_car = rental_car
            booking.user = request.user
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.pk)
    else:
        form = BookingForm()
    
    return render(request, 'customer/rental_cars/book_car.html', {'form': form, 'rental_car': rental_car})

def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    return render(request, 'customer/rental_cars/booking_confirmation.html', {'booking': booking})


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'customer/rental_cars/booking_list.html', {'bookings': bookings})


def update_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    form = BookingForm(instance=booking)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    
    return render(request, 'customer/rental_cars/update_booking.html', {'form': form})

def delete_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    
    return render(request, 'customer/rental_cars/delete_booking.html', {'booking': booking})

def user_logout(request):
    logout(request)
    return redirect('home')  