from django.contrib import admin

# Register your models here.
from WebApp.models import Employeee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["Empid","FirstName","LastName"]
admin.site.register(Employeee,EmployeeAdmin)