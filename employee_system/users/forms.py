from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Employee


class EmployeeSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = [
            "username",
            "name",
            "email",
            "employee_id",
            "mobile",
            "address",
            "gender",
            "password1",
            "password2",
        ]


class EmployeeUpdateForm(UserChangeForm):
    password = None  # hide password field

    class Meta:
        model = Employee
        fields = ["name", "email", "mobile", "address"]
