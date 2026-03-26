from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.db.models import Q
from django.core.paginator import Paginator

#registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required(login_url='login')

def home(request):
    query = request.GET.get('search', '')
    
    if query:
        
        employee_list = Employee.objects.filter(
            Q(emp_id__icontains=query) | 
            Q(emp_name__icontains=query) | 
            Q(emp_dept__icontains=query)
        ).order_by('-id') 
    else:
        employee_list = Employee.objects.all().order_by('-id')

    
    paginator = Paginator(employee_list, 5) 
    page_number = request.GET.get('page')
    employee_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'employee': employee_obj, 
        'query': query
    })

def create_view(request):
    return render(request, 'create.html')

def create_emp(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        emp_name = request.POST.get('emp_name')
        emp_dept = request.POST.get('emp_dept')

        if emp_id and emp_name and emp_dept:
            Employee.objects.create(emp_id=emp_id, emp_name=emp_name, emp_dept=emp_dept)
            messages.success(request, f"Employee {emp_name} has been added successfully!")
        return redirect('home')
    return render(request, 'create.html')

def update_view(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'update.html', {'employee': employee})

def update_emp(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.emp_id = request.POST.get('emp_id', employee.emp_id)
        employee.emp_name = request.POST.get('emp_name', employee.emp_name)
        employee.emp_dept = request.POST.get('emp_dept', employee.emp_dept)
        employee.save()
        return redirect('home')
    return render(request, 'update.html', {'employee': employee})

def delete_emp(request, id):
    employee = get_object_or_404(Employee, id=id)
    name = employee.emp_name
    employee.delete()
    messages.warning(request, f"Employee {name} was deleted successfully!")
    return redirect('home')