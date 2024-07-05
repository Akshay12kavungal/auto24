from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from admin_management.forms import LoginForm
from customer_management.forms import UserForm
from customer_management.models import Notification, ServiceRequest
from .models import Mechanic, MechanicEarnings, MechanicWork
from .forms import MechanicForm, UpdateWorkStatusForm
from django.contrib.auth import authenticate, login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def signup_mechanic(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        mechanic_form = MechanicForm(request.POST, request.FILES)
        if user_form.is_valid() and mechanic_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password1'])
            user.save()
            mechanic = mechanic_form.save(commit=False)
            mechanic.user = user
            mechanic.save()
            return redirect('login_mechanic')
    else:
        user_form = UserForm()
        mechanic_form = MechanicForm()
    return render(request, 'registrations/signup_mechanic.html', {'user_form': user_form, 'mechanic_form': mechanic_form})


def login_mechanic(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and hasattr(user, 'mechanic'):
                login(request, user)
                return redirect('mechanic_home')  # Redirect to mechanic dashboard after successful login
            else:
                return render(request, 'registrations/login_mechanic.html', {'form': form, 'error_message': 'Invalid username or password.'})
    else:
        form = LoginForm()
    return render(request, 'registrations/login_mechanic.html', {'form': form})

@login_required
def mechanic_home(request):
    mechanic = Mechanic.objects.get(user=request.user)
    works = ServiceRequest.objects.filter(works__mechanic=mechanic)
    return render(request, 'mechanic/mechanic_home.html', {'works': works})


@login_required
def assigned_work(request):
    mechanic = request.user.mechanic  # Assuming the logged-in user is a mechanic
    assigned_work = MechanicWork.objects.filter(mechanic=mechanic).order_by('-assigned_at')

    paginator = Paginator(assigned_work, 10)  # Show 10 notifications per page
    page = request.GET.get('page')

    try:
        assigned_work = paginator.page(page)
    except PageNotAnInteger:
        assigned_work = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        assigned_work = paginator.page(paginator.num_pages)  # If page is out of range (e.g. 9999), deliver last page of results.
    return render(request, 'mechanic/assigned_work.html', {'assigned_work': assigned_work})


@login_required
def update_work_status(request, pk):
    mechanic = get_object_or_404(Mechanic, user=request.user)
    work = get_object_or_404(MechanicWork, pk=pk, mechanic=mechanic)

    if request.method == 'POST':
        form = UpdateWorkStatusForm(request.POST, instance=work)
        if form.is_valid():
            work = form.save(commit=False)
            service_request = work.service_request
            
            if work.status == 'Released' and not MechanicEarnings.objects.filter(service_request=service_request).exists():
                service_request.status = work.status
                service_request.cost = form.cleaned_data['cost']
                service_request.save()
                
                mechanic_earnings = MechanicEarnings.objects.create(
                    mechanic=mechanic.user,
                    amount=form.cleaned_data['cost'],
                    service_request=service_request
                )

                message = f"Your service request status has been updated to {service_request.status}."
                Notification.objects.create(recipient=service_request.customer.user, message=message)

            work.save()
            return redirect('assigned_work')
    else:
        form = UpdateWorkStatusForm(instance=work)
    
    return render(request, 'mechanic/update_work_status.html', {'form': form, 'work': work})


@login_required
def view_mechanic_profile(request):
    mechanic = Mechanic.objects.get(user=request.user)
    return render(request, 'mechanic/mechanic_profile.html', {'mechanic': mechanic})

@login_required
def update_mechanic_profile(request):
    mechanic = Mechanic.objects.get(user=request.user)
    if request.method == 'POST':
        form = MechanicForm(request.POST, request.FILES, instance=mechanic)
        if form.is_valid():
            form.save()
            return redirect('view_mechanic_profile')
    else:
        form = MechanicForm(instance=mechanic)
    return render(request, 'mechanic/update_mechanic_profile.html', {'form': form})



@login_required
def completed_work(request):
    mechanic = get_object_or_404(Mechanic, user=request.user)
    
    completed_works = MechanicWork.objects.filter(
        mechanic=mechanic, 
        status__in=['Repairing Done', 'Released']
    ).order_by('-assigned_at')  # Order by assigned_at in descending order
    
    unique_service_requests = []
    unique_completed_work = []

    for work in completed_works:
        if work.service_request not in unique_service_requests:
            unique_service_requests.append(work.service_request)
            unique_completed_work.append(work)

    paginator = Paginator(unique_completed_work, 10)  # Show 10 items per page
    page = request.GET.get('page')

    try:
        completed_work = paginator.page(page)
    except PageNotAnInteger:
        completed_work = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        completed_work = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page of results.

    return render(request, 'mechanic/completed_work.html', {'completed_work': completed_work})
@login_required
def view_earnings(request):
    mechanic_earnings = MechanicEarnings.objects.filter(mechanic=request.user).order_by('-created_at')

    paginator = Paginator(mechanic_earnings, 4)  # Show 10 items per page
    page = request.GET.get('page')

    try:
        mechanic_earnings = paginator.page(page)
    except PageNotAnInteger:
        mechanic_earnings = paginator.page(1)  # If page is not an integer, deliver first page.
    except EmptyPage:
        mechanic_earnings = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page of results.

    return render(request, 'mechanic/earnings.html', {'mechanic_earnings': mechanic_earnings})



def mechanic_logout(request):
    logout(request)
    return redirect('home')  