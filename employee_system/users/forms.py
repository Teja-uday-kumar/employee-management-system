from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Employee
import re

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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Enter a valid email address.")
        # Allow only popular domains, modify as needed
        allowed_domains = ['gmail.com', 'yahoo.com', 'outlook.com']
        domain = email.split('@')[-1].lower()
        if domain not in allowed_domains:
            raise forms.ValidationError("Email domain is not allowed.")
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '')
        if not re.match(r"^\d{10,15}$", mobile):
            raise forms.ValidationError("Enter a valid mobile number (10-15 digits, digits only).")
        return mobile

class EmployeeUpdateForm(UserChangeForm):
    password = None  # hide the password field

    class Meta:
        model = Employee
        fields = ["name", "email", "mobile", "address"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Enter a valid email address.")
        allowed_domains = ['gmail.com', 'yahoo.com', 'outlook.com']
        domain = email.split('@')[-1].lower()
        if domain not in allowed_domains:
            raise forms.ValidationError("Email domain is not allowed.")
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile', '')
        if not re.match(r"^\d{10,15}$", mobile):
            raise forms.ValidationError("Enter a valid mobile number (10-15 digits, digits only).")
        return mobile
