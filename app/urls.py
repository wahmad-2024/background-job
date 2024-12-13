from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeViewSet

router = DefaultRouter()
router.register('start_job', HomeViewSet, basename="start_job")

urlpatterns = [
    path('', include(router.urls)),  
]
