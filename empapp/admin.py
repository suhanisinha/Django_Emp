from django.contrib import admin
from .models import Employee, Department
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["empID", "empName", "empDept", "empAddress"]

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["deptID", "deptName", "deptDesc"]

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)