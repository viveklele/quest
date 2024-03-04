from django.db import models

class Questions(models.Model):
    subject_code = models.CharField(max_length=250)
    question_text = models.TextField()
    toughness = models.CharField(max_length=50)
    is_selected = models.BooleanField()
    created_by = models.CharField(max_length=100)
    date_added = models.DateField()

    def __str__(self):
        return self.subject_code

class SubjectTable(models.Model):
    subject_code = models.IntegerField()
    subject_name = models.CharField(max_length=250)
    department_name = models.CharField(max_length=250)

    def __str__(self):
        return self.subject_name

class FacultyName(models.Model):
    faculty_id = models.IntegerField()
    name = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Exam(models.Model):
    exam_id = models.IntegerField()
    subject_code = models.CharField(max_length=50)
    exam_date = models.DateField()
    total_questions = models.IntegerField()
    duration = models.IntegerField()
    
    def __self__(self):
        return self.subject_code

