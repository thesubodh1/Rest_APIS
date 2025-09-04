from django.shortcuts import render,get_object_or_404
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics,viewsets

# Create your views here.

# creating class based views with viewsets using Routers
class Employees(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
