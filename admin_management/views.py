from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from admin_management.forms import LoginForm, RentalCarForm
from admin_management.models import RentalCar
from customer_management.forms import CustomerForm, UserForm
from customer_management.models import Customer, Vehicle, ServiceRequest, Feedback
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

from mechanic_management.models import Mechanic, MechanicWork
from mechanic_management.forms import MechanicForm

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
    customers = Customer.objects.all()
    mechanics = Mechanic.objects.all()
    service_requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'adminpage/admin_home.html', {'customers': customers, 'mechanics': mechanics, 'service_requests': service_requests})

@staff_member_required
def manage_customers(request):
    customers = Customer.objects.all()
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

@staff_member_required
def manage_mechanics(request):
    mechanics = Mechanic.objects.all()
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
    service_requests = ServiceRequest.objects.all()
    return render(request, 'adminpage/manage_service_requests.html', {'service_requests': service_requests})

@staff_member_required
def approve_service_request(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk)
    service_request.status = 'Approved'
    service_request.save()
    return redirect('manage_service_requests')

@staff_member_required
def assign_mechanic(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk)
    mechanics = Mechanic.objects.filter(status=True)
    if request.method == 'POST':
        mechanic_id = request.POST.get('mechanic')
        mechanic = Mechanic.objects.get(pk=mechanic_id)
        MechanicWork.objects.create(mechanic=mechanic, service_request=service_request, status='Repairing')
        service_request.status = 'Repairing'
        service_request.save()
        return redirect('manage_service_requests')
    return render(request, 'adminpage/assign_mechanic.html', {'service_request': service_request, 'mechanics': mechanics})


def rental_car_list(request):
    rental_cars = RentalCar.objects.all()
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


def admin_logout(request):
    logout(request)
    return redirect('home')