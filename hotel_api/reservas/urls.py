from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitacionViewSet, ReservaViewSet, verificar_disponibilidad, crear_resena

router = DefaultRouter()
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('disponibilidad/', verificar_disponibilidad),
    path('resenas/', crear_resena),
]
