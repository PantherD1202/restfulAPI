from rest_framework import viewsets
from .models import Employee, Student, Device, Car
from .serializers import EmployeeSerializer, StudentSerializer, DeviceSerializer, CarSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()                     # Lấy tất cả các bản ghi từ bảng cars
    serializer_class = CarSerializer