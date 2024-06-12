from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import Customer, Mechanic, MechanicWork, ServiceRequest, Feedback, Vehicle
from .forms import LoginForm, UpdateWorkStatusForm, UserForm, CustomerForm, MechanicForm, ServiceRequestForm, FeedbackForm, VehicleForm,LoginForm
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    return render(request, 'home.html')

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

def signup_mechanic(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        mechanic_form = MechanicForm(request.POST, request.FILES)
        if user_form.is_valid() and mechanic_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            mechanic = mechanic_form.save(commit=False)
            mechanic.user = user
            mechanic.save()
            return redirect('login_mechanic')
    else:
        user_form = UserForm()
        mechanic_form = MechanicForm()
    return render(request, 'registrations/signup_mechanic.html', {'user_form': user_form, 'mechanic_form': mechanic_form})

def login_customer(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.customer is not None:
                login(request, user)
                return redirect('customer_home')  # Redirect to customer dashboard after successful login
            else:
                return render(request, 'registrations/login_customer.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registrations/login_customer.html', {'form': form})

def login_mechanic(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.mechanic is not None:
                login(request, user)
                return redirect('mechanic_home')  # Redirect to mechanic dashboard after successful login
            else:
                return render(request, 'registrations/login_mechanic.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registrations/login_mechanic.html', {'form': form})

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

def admin_logout(request):
    logout(request)
    return redirect('home')

def user_logout(request):
    logout(request)
    return redirect('home')  

def mechanic_logout(request):
    logout(request)
    return redirect('home')  

#customer
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

@login_required
def customer_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user.customer
            feedback.save()
            return redirect('customer_home')
    else:
        form = FeedbackForm()
    return render(request, 'customer/customer_feedback.html', {'form': form})

#mechanic
@login_required
def mechanic_home(request):
    mechanic = Mechanic.objects.get(user=request.user)
    works = ServiceRequest.objects.filter(works__mechanic=mechanic)
    return render(request, 'mechanic/mechanic_home.html', {'works': works})


@login_required
def assigned_work(request):
    mechanic = request.user.mechanic  # Assuming the logged-in user is a mechanic
    assigned_work = MechanicWork.objects.filter(mechanic=mechanic)
    return render(request, 'mechanic/assigned_work.html', {'assigned_work': assigned_work})

@login_required
def update_work_status(request, pk):
    mechanic = get_object_or_404(Mechanic, user=request.user)
    work = get_object_or_404(MechanicWork, pk=pk, mechanic=mechanic)
    if request.method == 'POST':
        form = UpdateWorkStatusForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('assigned_work')
    else:
        form = UpdateWorkStatusForm(instance=work)
    return render(request, 'mechanic/update_work_status.html', {'form': form, 'work': work})

@login_required
def mechanic_profile(request):
    mechanic = Mechanic.objects.get(user=request.user)
    if request.method == 'POST':
        form = MechanicForm(request.POST, request.FILES, instance=mechanic)
        if form.is_valid():
            form.save()
            return redirect('mechanic_home')
    else:
        form = MechanicForm(instance=mechanic)
    return render(request, 'mechanic/mechanic_profile.html', {'form': form})

@login_required
def mechanic_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user.mechanic
            feedback.save()
            return redirect('mechanic_home')
    else:
        form = FeedbackForm()
    return render(request, 'mechanic/mechanic_feedback.html', {'form': form})

#admin
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




