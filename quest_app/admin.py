from django.contrib import admin
from .models import Questions, SubjectTable, FacultyName, Exam
# Register your models here.
admin.site.register(Questions)
admin.site.register(SubjectTable)
admin.site.register(FacultyName)
admin.site.register(Exam)