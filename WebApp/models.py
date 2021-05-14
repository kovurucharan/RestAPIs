from django.db import models

# Create your models here.
class Employeee(models.Model):
    Empid=models.IntegerField()
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName