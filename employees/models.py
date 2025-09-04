from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=5, unique=True,db_index=True)
    employee_name = models.CharField(max_length=100)
    employees_position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee_id}, {self.employee_name}"
    
class Remarks(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="remarks")
    remark = models.TextField()

    def __str__(self):
        return f"{self.employee}, {self.remark}"
