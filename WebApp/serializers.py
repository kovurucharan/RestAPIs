from WebApp.models import Employeee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employeee
        fields=["Empid","FirstName","LastName"]