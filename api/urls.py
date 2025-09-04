from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('employees',views.Employees,basename='employee')

urlpatterns = [
    # path("employees/",views.Employees.as_view()),
    # path("employees/<int:pk>/",views.EmployeesDetails.as_view())
    # path('',include(router.urls)),

    path("employees/",views.Employees.as_view()),
    path("employees/<int:pk>",views.EmployeesDetail.as_view()),
    path("remarks/",views.RemarksView.as_view()),
    path("remarks/<int:pk>",views.RemarksDetail.as_view())
]
