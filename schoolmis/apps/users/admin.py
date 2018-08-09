from django.contrib import admin
from .models import StudentProfile, ParentProfile, TeacherProfile

admin.site.register(StudentProfile)

admin.site.register(ParentProfile)

admin.site.register(TeacherProfile)
