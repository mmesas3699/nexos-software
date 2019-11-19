# Create your views here.

from crud.models import Score, Student, Professor
from rest_framework import viewsets
from .serializers import ScoreSerializer, StudentSerializer, ProfessorSerializer


class ScoreViewSet(viewsets.ModelViewSet):

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer


class ProfessorViewSet(viewsets.ModelViewSet):

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
