from django.urls import path
from . import views

urlpatterns = [
    path("employees/",views.Employees.as_view()),
    path("employees/<int:pk>/",views.EmployeesDetails.as_view())
]
