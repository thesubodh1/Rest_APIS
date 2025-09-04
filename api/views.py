from django.shortcuts import render,get_object_or_404
from employees.models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins,generics,viewsets

# Create your views here.

# creating class based views with viewsets using Routers
class Employees(viewsets.ViewSet):
   def list(self,request):
      employee = Employee.objects.all()
      serializer = EmployeeSerializer(employee,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)
   
   def create(self,request):
      serializer = EmployeeSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      else:
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
   def retrieve(self,request,pk):
      employee = Employee.objects.get(pk=pk)
      serializer = EmployeeSerializer(employee)
      return Response(serializer.data, status=status.HTTP_200_OK)
   
   def update(self,request,pk):
      employee = Employee.objects.get(pk=pk)
      serializer = EmployeeSerializer(employee,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
      else:
         return Response(status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self,request,pk):
      employee = Employee.objects.get(pk=pk)
      employee.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    
