from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse

from .models import Attendance, MarkSheet, Mark
from .forms import MarkSheetForm, AttendanceForm, MarkForm


class MarkSheetMixin(LoginRequiredMixin):
    model = MarkSheet
    form_class = MarkSheetForm
    context_object_name = 'marksheet'

    def get_success_url(self):
        return reverse('reportcard:marksheet_list')


class AttendanceMixin(LoginRequiredMixin):
    model = Attendance
    form_class = AttendanceForm
    context_object_name = 'attendance'

    def get_success_url(self):
        return reverse('reportcard:attendance_list')


class MarkMixin(LoginRequiredMixin):
    model = Mark
    form_class = MarkForm
    context_object_name = 'mark'

    def get_success_url(self):
        return reverse('reportcard:mark_list')
