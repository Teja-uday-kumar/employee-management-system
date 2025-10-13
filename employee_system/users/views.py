from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EmployeeSignupForm, EmployeeUpdateForm
from .models import Employee

def signup_view(request):
    if request.method == "POST":
        form = EmployeeSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the highlighted errors.")
    else:
        form = EmployeeSignupForm()
    return render(request, "users/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("employee_list")
        else:
            messages.error(request, "Invalid login credentials.")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "users/employee_list.html", {"employees": employees})

@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    # Allow user to edit themselves OR staff/admins to edit anyone
    if request.user != employee and not request.user.is_staff:
        messages.error(request, "You can only edit your own profile or must be an admin.")
        return redirect("employee_list")

    if request.method == "POST":
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("employee_list")
        else:
            messages.error(request, "Please correct the highlighted errors.")
    else:
        form = EmployeeUpdateForm(instance=employee)

    return render(request, "users/edit_employee.html", {"form": form, "employee": employee})

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    is_self = request.user == employee

    # Allow user to delete themselves OR staff/admins to delete anyone
    if not is_self and not request.user.is_staff:
        messages.error(request, "You can only delete your own profile or must be an admin.")
        return redirect("employee_list")

    if request.method == "POST":
        employee.delete()
        if is_self:
            logout(request)
            messages.success(request, "Your account has been deleted and you have been logged out.")
            return redirect("login")
        else:
            messages.success(request, "Employee deleted successfully.")
            return redirect("employee_list")

    return render(request, "users/delete_employee.html", {"employee": employee})
