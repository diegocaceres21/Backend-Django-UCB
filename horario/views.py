from rest_framework import viewsets
from .serializer import HorarioSerializer, OpcionSerializer
from .models import Horario, Opcion
# Create your v     iews here.

class HorarioView(viewsets.ModelViewSet):
    serializer_class = HorarioSerializer
    queryset = Horario.objects.all()
    def get_queryset(self):
        queryset = self.queryset
        sigla = self.request.query_params.get('sigla')
        asignatura = self.request.query_params.get('asignatura')

        if sigla:
            queryset = queryset.filter(sigla=sigla)
        if asignatura:
            queryset = queryset.filter(horario=asignatura)

        return queryset

class OpcionView(viewsets.ModelViewSet):
    serializer_class = OpcionSerializer
    queryset = Opcion.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        carrera = self.request.query_params.get('carrera')
        opcion = self.request.query_params.get('opcion')

        if carrera:
            queryset = queryset.filter(carrera=carrera)
        if opcion:
            queryset = queryset.filter(horario=opcion)

        return queryset