from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import EmployeeSignupForm, EmployeeUpdateForm
from .models import Employee


def signup_view(request):
    if request.method == "POST":
        form = EmployeeSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("employee_list")
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
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
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
        return redirect("employee_list")

    if request.method == "POST":
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeUpdateForm(instance=employee)

    return render(request, "users/edit_employee.html", {"form": form, "employee": employee})


@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    # Allow user to delete themselves OR staff/admins to delete anyone
    if request.user != employee and not request.user.is_staff:
        return redirect("employee_list")

    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")

    return render(request, "users/delete_employee.html", {"employee": employee})
