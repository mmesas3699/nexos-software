from .models import Score, Student, Professor
from rest_framework import serializers


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['name']


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ['name', 'value', 'student_id', 'professor_id']


class StudentSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['name', 'scores']
