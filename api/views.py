from django.shortcuts import render,get_object_or_404
from employees.models import Employee,Remarks
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics,viewsets
from employees.serializers import RemarksSerializer,EmployeeSerializer
from .pagination import CustomPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from employees.filters import EmployeeFilter
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# creating class based views with nested serializers
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
   #  pagination_class = CustomPagination
    # filterset_fields = ['employee_name',"employees_position"]
    filterset_class = EmployeeFilter
    filter_backends = [SearchFilter, DjangoFilterBackend,OrderingFilter] #  for search
    search_fields = ["employee_name"] # can add multiple
    ordering_fields = ["employee_id"]
    


class RemarksView(generics.ListCreateAPIView):
    queryset = Remarks.objects.all()
    serializer_class = RemarksSerializer
   #  pagination_class = CustomPagination


class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"
   #  pagination_class = CustomPagination


class RemarksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Remarks.objects.all()
    serializer_class = RemarksSerializer
    lookup_field = "pk"
   #  pagination_class = CustomPagination


