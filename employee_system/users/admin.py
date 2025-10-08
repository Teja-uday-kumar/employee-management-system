from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee

class EmployeeAdmin(UserAdmin):
    model = Employee
    list_display = ("username", "name", "employee_id", "email", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('employee_id', 'name', 'mobile', 'address', 'gender')}),
    )

admin.site.register(Employee, EmployeeAdmin)
