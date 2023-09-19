from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from horario import views

router = routers.DefaultRouter()
router.register(r'horarios', views.HorarioView, 'horario')
router.register(r'opciones', views.OpcionView, 'horario')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title="API de Horarios UCB"))
]
