from django import template
from django.core.exceptions import PermissionDenied

from apps.reportcard.models import Subject
from apps.users.models import StudentProfile

register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='student_subjects')
def student_subjects(request):
    return Subject.objects.select_related().filter(grade=request.user.student_profile.grade)


@register.filter(name='teacher_subjects')
def teacher_subjects(request):
    return Subject.objects.select_related().filter(teacher=request.user.teacher_profile)


@register.filter(name='parent_children')
def parent_children(request):
    return StudentProfile.objects.select_related().filter(parent=request.user.parent_profile)


@register.filter
def subtract(value, arg):
    return value - arg