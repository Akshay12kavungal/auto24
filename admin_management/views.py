from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from admin_management.forms import LoginForm, RentalCarForm
from admin_management.models import Booking, RentalCar
from customer_management.forms import CustomerForm, UserForm
from customer_management.models import Customer, Notification, Vehicle, ServiceRequest, Feedback
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

from mechanic_management.models import Mechanic, MechanicWork
from mechanic_management.forms import MechanicForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'home.html')


def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('admin_home')  # Redirect to the admin dashboard after successful login
            else:
                # Invalid login credentials
                return render(request, 'admin/login.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registrations/login_admin.html', {'form': form})


@staff_member_required
def admin_home(request):
    total_customers = Customer.objects.count()
    total_mechanics = Mechanic.objects.count()
    total_service_requests = ServiceRequest.objects.count()
    total_car_rentals = Booking.objects.count()  # Assuming you have a CarRental model

    customers = Customer.objects.all()[:5]  # Get the latest 5 customers
    mechanics = Mechanic.objects.all()[:5]  # Get the latest 5 mechanics
    service_requests = ServiceRequest.objects.all()[:5]  # Get the latest 5 service requests

    context = {
        'total_customers': total_customers,
        'total_mechanics': total_mechanics,
        'total_service_requests': total_service_requests,
        'total_car_rentals': total_car_rentals,
        'customers': customers,
        'mechanics': mechanics,
        'service_requests': service_requests,
    }
    
    return render(request, 'adminpage/admin_home.html', context)

#customer manage

@staff_member_required
def manage_customers(request):
    customers = Customer.objects.order_by('created_at')
    paginator = Paginator(customers, 10)  # Show 4 rental cars per page
    page = request.GET.get('page')

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page.
    return render(request, 'adminpage/manage_customers.html', {'customers': customers})

@staff_member_required
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=customer.user)
        customer_form = CustomerForm(request.POST, request.FILES, instance=customer)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            return redirect('manage_customers')
    else:
        user_form = UserForm(instance=customer.user)
        customer_form = CustomerForm(instance=customer)
    return render(request, 'adminpage/add_edit_customer.html', {'user_form': user_form, 'customer_form': customer_form})

@staff_member_required
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.user.delete()  # This will also delete the customer due to the on_delete setting
        return redirect('manage_customers')
    return render(request, 'adminpage/delete_customer.html', {'customer': customer})


#manage mechanic
@staff_member_required
def manage_mechanics(request):
    mechanics = Mechanic.objects.order_by('-created_at')

    paginator = Paginator(mechanics, 10)  # Show 4 rental cars per page
    page = request.GET.get('page')

    try:
        mechanics = paginator.page(page)
    except PageNotAnInteger:
        mechanics = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        mechanics = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page.
    return render(request, 'adminpage/manage_mechanics.html', {'mechanics': mechanics})


@staff_member_required
def edit_mechanic(request, pk):
    mechanic = get_object_or_404(Mechanic, pk=pk)
    if request.method == 'POST':
        form = MechanicForm(request.POST, request.FILES, instance=mechanic)
        if form.is_valid():
            form.save()
            return redirect('manage_mechanics')
    else:
        form = MechanicForm(instance=mechanic)
    return render(request, 'adminpage/edit_mechanic.html', {'form': form})

@staff_member_required
def delete_mechanic(request, pk):
    mechanic = get_object_or_404(Mechanic, pk=pk)
    mechanic.user.delete()  # This will also delete the mechanic profile due to the OneToOne relationship
    return redirect('manage_mechanics')




@staff_member_required
def approve_mechanic(request, pk):
    mechanic = Mechanic.objects.get(pk=pk)
    mechanic.status = True
    mechanic.save()
    return redirect('manage_mechanics')

@staff_member_required
def manage_service_requests(request):
    service_requests = ServiceRequest.objects.order_by('-created_at')
    paginator = Paginator(service_requests, 10)  # Show 10 service requests per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'adminpage/manage_service_requests.html', {'page_obj': page_obj})



@staff_member_required
def approve_service_request(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk)
    service_request.status = 'Approved'
    service_request.save()
    message = f"Your service request status has been updated to {service_request.status}."
    Notification.objects.create(recipient=service_request.customer.user, message=message)
    return redirect('manage_service_requests')


@staff_member_required
def delete_service_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    if request.method == 'POST':
        service_request.delete()
        return redirect('manage_service_requests')
    return render(request, 'adminpage/delete_service.html', {'service_request': service_request})




@staff_member_required
def assign_mechanic(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    mechanics = Mechanic.objects.filter(status=True)
    
    if request.method == 'POST':
        mechanic_id = request.POST.get('mechanic')
        mechanic = get_object_or_404(Mechanic, pk=mechanic_id)
        
        # Update MechanicWork instance and service request status
        MechanicWork.objects.create(mechanic=mechanic, service_request=service_request, status='Repairing')
        service_request.status = 'Repairing'
        service_request.assigned_mechanic = mechanic  # Assign the mechanic to the service request
        service_request.save()
        
        # Create notification message
        message = f"Your service request status has been updated to {service_request.status}, assigned to {mechanic.user.get_full_name()}."
        Notification.objects.create(recipient=service_request.customer.user, message=message)
        
        return redirect('manage_service_requests')
    
    return render(request, 'adminpage/assign_mechanic.html', {'service_request': service_request, 'mechanics': mechanics})


#rental car
def rental_car_list(request):
    rental_cars = RentalCar.objects.order_by('-created_at')

    paginator = Paginator(rental_cars, 10)  # Show 4 rental cars per page
    page = request.GET.get('page')

    try:
        rental_cars = paginator.page(page)
    except PageNotAnInteger:
        rental_cars = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        rental_cars = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page.

    return render(request, 'adminpage/rental_cars/rental_car_list.html', {'rental_cars': rental_cars})

def add_rental_car(request):
    if request.method == 'POST':
        form = RentalCarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('rental_car_list')  # Redirect to list view after successful creation
    else:
        form = RentalCarForm()
    return render(request, 'adminpage/rental_cars/add_rental_car.html', {'form': form})

def edit_rental_car(request, pk):
    rental_car = get_object_or_404(RentalCar, pk=pk)
    if request.method == 'POST':
        form = RentalCarForm(request.POST, request.FILES, instance=rental_car)
        if form.is_valid():
            form.save()
            return redirect('rental_car_list')  # Redirect to list view after successful update
    else:
        form = RentalCarForm(instance=rental_car)
    return render(request, 'adminpage/rental_cars/edit_rental_car.html', {'form': form})

def delete_rental_car(request, pk):
    rental_car = get_object_or_404(RentalCar, pk=pk)
    if request.method == 'POST':
        rental_car.delete()
        return redirect('rental_car_list')  # Redirect to list view after successful deletion
    return render(request, 'adminpage/rental_cars/delete_rental_car.html', {'rental_car': rental_car})


def admin_pending_bookings(request):
    all_bookings = Booking.objects.order_by('-created_at')

    paginator = Paginator(all_bookings, 10) 
    page = request.GET.get('page')

    try:
        all_bookings = paginator.page(page)
    except PageNotAnInteger:
        all_bookings = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        all_bookings = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page.
    return render(request, 'adminpage/rental_cars/pending_bookings.html', {'all_bookings': all_bookings})

def admin_update_booking_status(request, booking_id, status):
    booking = get_object_or_404(Booking, pk=booking_id)
    if status in [Booking.ACCEPTED, Booking.REJECTED]:
        booking.status = status
        booking.save()
        message = f"Your booking for {booking.rental_car.name} has been {booking.status}."
        Notification.objects.create(recipient=booking.user, message=message)
    return redirect('admin_pending_bookings')

def admin_logout(request):
    logout(request)
    return redirect('home')