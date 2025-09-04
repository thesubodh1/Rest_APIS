from django.shortcuts import render,get_object_or_404
from employees.models import Employee,Remarks
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics,viewsets
from employees.serializers import RemarksSerializer,EmployeeSerializer
from .pagination import CustomPagination

# Create your views here.

# creating class based views with nested serializers
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination

class RemarksView(generics.ListCreateAPIView):
    queryset = Remarks.objects.all()
    serializer_class = RemarksSerializer
    pagination_class = CustomPagination


class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"
    pagination_class = CustomPagination


class RemarksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Remarks.objects.all()
    serializer_class = RemarksSerializer
    lookup_field = "pk"
    pagination_class = CustomPagination


