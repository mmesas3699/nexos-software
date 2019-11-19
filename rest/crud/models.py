from django.db import models

# Create your models here.


class Student(models.Model):
    """Student Model"""

    name = models.CharField(max_length=60, null=False, blank=False, default='Student')

    def __str__(self):
        return f"{self.name}"


class Professor(models.Model):
    """Professor Model"""

    name = models.CharField(max_length=60, null=False, blank=False, default='Professor')

    def __str__(self):
        return f"{self.name}"


class Score(models.Model):
    """Score model"""

    name = models.CharField(max_length=30, null=False, blank=False, default='Score')
    value = models.PositiveIntegerField(default=0, null=False, blank=False)
    professor_id = models.ForeignKey(Professor, on_delete=models.PROTECT, related_name='scores')
    student_id = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='scores')

    def __str__(self):
        return f"{self.name}: {self.value}"