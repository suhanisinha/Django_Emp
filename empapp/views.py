from django.shortcuts import render
from empapp.models import Employee, Department
from empapp.serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def search_employees(request):
    query = request.query_params.get("search")
    employees = Employee.objects.filter(Q(empName__icontains=query))
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def employees(request):
    if request.method == "GET":
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def departments(request):
    if request.method == "GET":
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)