from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    mssv = models.CharField(max_length=10, primary_key=True)  # Đặt mssv là khóa chính
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    class_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'students'  # Đảm bảo rằng tên bảng là 'students'

    def __str__(self):
        return self.name
    
class Device(models.Model):
    msp = models.CharField(max_length=10, primary_key=True)  # Đặt mssv là khóa chính
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=50)

    class Meta:
        db_table = 'divices'  # Đảm bảo rằng tên bảng là 'students'

    def __str__(self):
        return self.name