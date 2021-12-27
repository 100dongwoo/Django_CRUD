from django.db import models


# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100, null=True)
    emp_code = models.CharField(max_length=3, null=True)
    mobile = models.CharField(max_length=15, null=True)