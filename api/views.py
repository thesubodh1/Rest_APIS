from django.shortcuts import render,get_object_or_404
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics

# Create your views here.

# creating class based views with generics
class Employees(generics.ListAPIView,generics.CreateAPIView):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer
    
class EmployeesDetails(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer
   lookup_field = "pk"
