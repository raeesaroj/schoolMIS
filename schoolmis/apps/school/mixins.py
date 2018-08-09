from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse

from .models import Grade, ExamType
from .forms import ExamTypeForm


class GradeMixin(LoginRequiredMixin):
    model = Grade
    fields = ['name']
    context_object_name = 'grade'

    def get_success_url(self):
        return reverse('school:grade_list')


class ExamTypeMixin(LoginRequiredMixin):
    model = ExamType
    form_class = ExamTypeForm
    context_object_name = 'exam_type'

    def get_success_url(self):
        return reverse('school:exam_type_list')