from rest_framework import serializers
from .models import Employee, Department

class EmployeeSerializer(serializers.ModelSerializer):
    # empDept = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = ["empID", "empName", "empDept", "empAddress"]

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["deptID", "deptName", "deptDesc"]