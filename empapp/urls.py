from django.urls import path 
from .import views 


urlpatterns = [
    path("employees/", views.employees, name="employees"),
    path("departments/", views.departments, name="departments"),
    path("search-employees/", views.search_employees, name="search-employees")
]