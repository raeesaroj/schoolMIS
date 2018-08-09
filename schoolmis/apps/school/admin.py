from django.contrib import admin

from .models import Grade, Section, ExamType
from apps.reportcard.models import Subject


class SectionInline(admin.TabularInline):
    model = Section
    extra = 0
    fields = ["name", "class_teacher"]


class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 0
    fields = ["name", "code", "exam_type",
              "teacher", "full_marks", "pass_marks"]


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    fields = ['name']
    inlines = [SectionInline, SubjectInline]


admin.site.register(ExamType)
