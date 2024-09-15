from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.department
    

class Semester(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return f"{self.department},  {self.semester}"


class Section(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    section = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return f"{self.semester},{self.section}"


class Subject(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name  = models.CharField(max_length=100, null=True, blank=True)

    
class Student(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=250, unique=True)
    stu_name = models.CharField(max_length=250, null=True, blank=True)
    stu_father_name = models.CharField(max_length=250, null=True, blank=True)
    cnic_no = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.student_id

class Professor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    section = models.ManyToManyField(Section)
    subject = models.ManyToManyField(Subject)
    teacher_id = models.CharField(max_length=250, null=True, blank=True)
    name =  models.CharField(max_length=250, null=True, blank=True)


