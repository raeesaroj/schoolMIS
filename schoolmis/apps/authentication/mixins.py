from django.shortcuts import reverse

from apps.users.models import ParentProfile, TeacherProfile, StudentProfile
from .forms import TeacherSignupForm, StudentSignupForm, ParentSignupForm


class ParentMixin(object):
    model = ParentProfile
    context_object_name = 'parent'
    form_class = ParentSignupForm

    def get_success_url(self):
        return reverse('authentication:parent_list')


class TeacherMixin(object):
    model = TeacherProfile
    form_class = TeacherSignupForm
    context_object_name = 'teacher'

    def get_success_url(self):
        return reverse('authentication:teacher_list')


class StudentMixin(object):
    model = StudentProfile
    form_class = StudentSignupForm
    context_object_name = 'students'

    def get_success_url(self):
        return reverse('authentication:student_list')
