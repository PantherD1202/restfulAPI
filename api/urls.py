from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, StudentViewSet, DeviceViewSet, CarViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'students', StudentViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
