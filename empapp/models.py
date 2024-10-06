from django.db import models

# Create your models here.
class Department(models.Model):
    deptID = models.IntegerField(default=0, null=False)
    deptName = models.CharField(max_length=100) 
    deptDesc = models.TextField()

    def __str__(self):
        return self.deptName
        
class Employee(models.Model):
    empID = models.IntegerField(default=0, null=False)
    empName = models.CharField(max_length=25)
    empDept = models.CharField(max_length=100) 
    empAddress = models.TextField()

    def __str__(self):
        return str(self.empID) + ' | ' + self.empName 
        