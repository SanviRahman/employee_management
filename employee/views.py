from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Home view to display all employees
def home(request):
    employees = Employee.objects.all()
    return render(request, 'employee/home.html', {'employees': employees})

# Add Employee
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employee/add_employee.html', {'form': form})

# Update Employee
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)

    # Ensure Designation and Salary fields are non-editable
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'employee/update_employee.html', {'form': form})

# Delete Employee
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')
    return render(request, 'employee/delete_employee.html', {'employee': employee})
