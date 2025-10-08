from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Employee(AbstractUser):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=(("Male", "Male"), ("Female", "Female"), ("Other", "Other")),
    )

    #  createsuperuser
    REQUIRED_FIELDS = ["email", "employee_id", "name"]

    def __str__(self):
        return f"{self.name} ({self.employee_id})"
