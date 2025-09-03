from django.shortcuts import render
from django.http import JsonResponse
from employees.models import Employee

# Create your views here.
def employees(request):
   employees = list(Employee.objects.all().values())
   return JsonResponse(employees,safe=False)
