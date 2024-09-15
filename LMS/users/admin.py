from django.contrib import admin
from .models import *
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department']


class SemesterAdmin(admin.ModelAdmin):
    list_display =['semester', 'department']
    list_filter =['department']


class SectionAdmin(admin.ModelAdmin):
    list_display = ['section', 'semester']
    list_filter = ['semester__department', 'semester']


class StudentAdmin(admin.ModelAdmin):
    list_display =['student_id', 'section']
    list_filter =['section__semester__department', 'section__semester', 'section']



admin.site.register(Department, DepartmentAdmin )
admin.site.register(Section, SectionAdmin)
admin.site.register(Semester, SemesterAdmin)

admin.site.register(Student, StudentAdmin)
admin.site.register(Professor)

