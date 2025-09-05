import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name="employee_name",lookup_expr="icontains")
    employee_position = django_filters.CharFilter(field_name="employees_position",lookup_expr="icontains")

    class Meta:
        model = Employee
        fields = ['employee_name','employee_position']