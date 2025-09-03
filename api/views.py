from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from employees.models import Employee
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# create function based views using decorators
@api_view(["GET","POST"])
def employees(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(["GET","PUT","DELETE"])
def employees_details(request,pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
