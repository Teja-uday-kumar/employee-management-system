from django.urls import path
from .views import signup_view, login_view, logout_view, employee_list, edit_employee,delete_employee

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/edit/<int:pk>/', edit_employee, name='edit_employee'),
    path('employees/<int:pk>/delete/', delete_employee, name='delete_employee'),
]
