import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name="employee_name",lookup_expr="icontains")
    employee_position = django_filters.CharFilter(field_name="employees_position",lookup_expr="icontains")
    id_max = django_filters.CharFilter(method='filter_by_id_range',label="To EMP ID")
    id_min = django_filters.CharFilter(method='filter_by_id_range',label="From EMP ID")

    class Meta:
        model = Employee
        fields = ['employee_name','employee_position','id_max','id_min']

    def filter_by_id_range(self,queryset,name,value):
        if name == "id_max":
            return queryset.filter(employee_id__lte = value)
        elif name == "id_min":
            return queryset.filter(employee_id__gte=value)
        return queryset