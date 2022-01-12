from django.db import models

# Create your models here.

class Employee(models.Model):
    Employee_Name = models.CharField(max_length=50)
    Employee_Address = models.CharField(max_length=200)
    Employee_Contact_Number = models.CharField(max_length=15)
    Employee_Email = models.EmailField()
    Employee_Age = models.DateField()

    def __str__(self):
        return self.Employee_Name
