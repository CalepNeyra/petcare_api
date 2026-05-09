from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DuenoViewSet, MascotaViewSet


router = DefaultRouter()
router.register(r'duenos', DuenoViewSet)
router.register(r'mascotas', MascotaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
