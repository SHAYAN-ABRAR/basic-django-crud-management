from django.shortcuts import render, redirect, get_object_or_404
from .models import Salary
from employee.models import Employee 
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def payroll_home(request):
    # Fetch all salary records to show in the table
    salaries = Salary.objects.select_related('employee').all()
    return render(request, 'payroll_home.html', {'salaries': salaries})


@login_required(login_url='login')
def add_salary(request):
    if request.method == 'POST':
        emp_id = request.POST.get('employee_id')
        amount = request.POST.get('amount')
        bonus = request.POST.get('bonus')
        pay_date = request.POST.get('pay_date')

        if emp_id and amount:
            employee = get_object_or_404(Employee, id=emp_id)
            Salary.objects.create(
                employee=employee,
                amount=amount,
                bonus=bonus,
                pay_date=pay_date
            )
            messages.success(request, f"Salary processed for {employee.emp_name}!")
            return redirect('payroll_home')
            
    employees = Employee.objects.all()
    return render(request, 'add_salary.html', {'employees': employees})

@login_required(login_url='login')
def edit_salary(request, pk):
    
    salary = get_object_or_404(Salary, pk=pk)
    
    employees = Employee.objects.all()

    if request.method == 'POST':
        emp_id = request.POST.get('employee_id')
        salary.amount = request.POST.get('amount')
        salary.bonus = request.POST.get('bonus')
        salary.pay_date = request.POST.get('pay_date')

        if emp_id:
            salary.employee = get_object_or_404(Employee, id=emp_id)
            salary.save()
            messages.success(request, f"Payment for {salary.employee.emp_name} updated!")
            return redirect('payroll_home')

    return render(request, 'edit_salary.html', {
        'salary': salary,
        'employees': employees
    })