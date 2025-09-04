from django.shortcuts import render,get_object_or_404
from employees.models import Employee,Remarks
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics,viewsets
from employees.serializers import RemarksSerializer,EmployeeSerializer

# Create your views here.

# creating class based views with nested serializers
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RemarksView(generics.ListCreateAPIView):
    queryset = Remarks.objects.all()
    serializer_class = RemarksSerializer

class EmployeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"

class RemarksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Remarks.objects.all()
    serializer_class = RemarksSerializer
    lookup_field = "pk"

