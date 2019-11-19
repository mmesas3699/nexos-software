# Register your models here.

from django.contrib import admin

from crud.models import Student, Score, Professor


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )
    list_filter = ('name',)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    fields = ('name', 'value', 'professor_id', 'student_id')
    list_display = ('name', 'value', 'professor_id', 'student_id')
    list_filter = ('name', 'value', 'professor_id__name', 'student_id__name')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )
    list_filter = ('name', )
