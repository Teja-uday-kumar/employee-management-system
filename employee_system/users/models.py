from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Employee(AbstractUser):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    # Validator only allows digits; changes on form can supplement further checks if needed
    mobile = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10,15}$',
                message='Enter a valid mobile number (10–15 digits, digits only).',
                code='invalid_mobile'
            )
        ]
    )
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(
        max_length=10,
        choices=(("Male", "Male"), ("Female", "Female"), ("Other", "Other")),
    )

    REQUIRED_FIELDS = ["email", "employee_id", "name"]

    def __str__(self):
        return f"{self.name} ({self.employee_id})"
