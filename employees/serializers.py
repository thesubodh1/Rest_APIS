from .models import Employee,Remarks
from rest_framework import serializers

class RemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remarks
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    remarks = RemarksSerializer(many=True,read_only=True)
    class Meta:
        model = Employee
        fields = "__all__"