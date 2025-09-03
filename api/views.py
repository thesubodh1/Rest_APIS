from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def employees(request):
    students = [
        {
            "name":"Subodh dahal",
            "batch" : "2019",
            "faculty" : "IT",
        },
        {
            "name":"Ramesh Yadav",
            "batch" : "2017",
            "faculty" : "Management"
        },
        {
            "name":"Suresh Bajgain",
            "batch":"2025",
            "faculty" : "Science",
        }
    ]
    return JsonResponse(students,safe=False)
