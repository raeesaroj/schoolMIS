import zipfile
from io import BytesIO
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.db.models import Q

from weasyprint import HTML
from dal import autocomplete

from libs.views_mixins_utils import QueryMixin, OwnerListMixin, OwnerMixin, OwnerCreateMixin
from apps.userrole.permissions import CheckPermissionCreateMixin, CheckPermissionUpdateMixin, CheckPermissionListMixin, \
    CheckPermissionDeleteMixin, CheckPermissionDetailMixin
from apps.users.models import StudentProfile
from .models import Subject, MarkSheet, Attendance
from .mixins import MarkSheetMixin, AttendanceMixin, MarkMixin
from .forms import StudentMarksFormSet


class StudentAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = StudentProfile.objects.all()
        grade = self.forwarded.get('grade', None)

        if grade:
            qs = qs.filter(grade=grade)
        if self.q:
            qs = qs.filter(Q(user__first_name__icontains=self.q) | Q(user__student_profile__roll_no=self.q))

        return qs


class SubjectListView(CheckPermissionListMixin, QueryMixin, ListView):
    model = Subject
    fields = '__all__'
    context_object_name = 'subjects'
    template_name = 'reportcard/subject_list.html'


class MarkSheetCreateView(CheckPermissionCreateMixin, MarkSheetMixin, OwnerCreateMixin, CreateView):
    template_name = 'reportcard/marksheet_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class MarkSheetListView(CheckPermissionListMixin, MarkSheetMixin, QueryMixin, ListView):
    template_name = 'reportcard/marksheet_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if self.request.user.groups.filter(name='Student'):
                context['marksheet'] = MarkSheet.objects.select_related().filter(student=self.request.user.
                                                                                 student_profile)
                return context

            elif self.request.user.groups.filter(name='Guardian'):

                context['marksheet'] = MarkSheet.objects.select_related().filter(
                        student__in=self.request.user.parent_profile.student_parent.all())
                return context

            elif self.request.user.groups.filter(name='Teacher'):

                context['marksheet'] = MarkSheet.objects.select_related().filter(
                        created_by=self.request.user)
                return context

            else:
                context['marksheet'] = MarkSheet.objects.select_related()
                return context

        except StudentProfile.DoesNotExist:
            pass


class MarkSheetDetailView(CheckPermissionDetailMixin, MarkSheetMixin, DetailView):

    def get_queryset(self):
        return super().get_queryset().select_related()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Student'):
            try:
                marksheet = MarkSheet.objects.filter(student=self.request.user.student_profile)
                context['marksheet'] = self.get_object(marksheet)
                return context
            except Http404:
                raise PermissionDenied

        elif self.request.user.groups.filter(name='Guardian'):
            try:
                marksheet = MarkSheet.objects.filter(student__in=self.request.user.parent_profile.student_parent.all())
                context['marksheet'] = self.get_object(marksheet)
                return context
            except Http404:
                raise PermissionDenied

        else:
            context['marksheet'] = self.get_object()
            if context['marksheet'].created_by != self.request.user:
                raise PermissionDenied
            return context


class MarkSheetUpdateView(CheckPermissionUpdateMixin, MarkSheetMixin, OwnerMixin, UpdateView):
    template_name = 'reportcard/marksheet_update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class MarkSheetDeleteView(CheckPermissionDeleteMixin, MarkSheetMixin, OwnerMixin, DeleteView):
    template_name = 'reportcard/marksheet_delete.html'


class MarkSheetPdfView(MarkSheetDetailView):

    def post(self, request, *args, **kwargs):
        marksheet = self.get_object()
        html_string = render_to_string('reportcard/marksheet_detail.html', {'marksheet': marksheet}, request=request)
        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/marksheet.pdf')
        fs = FileSystemStorage('/tmp')
        with fs.open('marksheet.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="marksheet.pdf"'
        return response


class MarkSheetPdfZipView(MarkSheetDetailView):

    def post(self, request, *args, **kwargs):
        marksheetlist = MarkSheet.objects.select_related().filter(created_by=self.request.user)
        zip_title = "archieve.zip"
        s = BytesIO()
        # zf = zipfile.ZipFile(s, "a")
        with zipfile.ZipFile(s, "a") as zf:
            for marksheet in marksheetlist:
                # print('****************' , marksheet)
                html_string = render_to_string('reportcard/marksheet_zip.html', {'marksheet': marksheet}, request=request)
                # print('****************html_string name***********', html_string)
                html = HTML(string=html_string)
                fileloc = '/tmp/grade_{}_{}_{}'.format(marksheet.grade, marksheet.student, marksheet.student.roll_no) + '.pdf'
                # print('this is fileloc' , fileloc)
                html.write_pdf(target=fileloc)
                zf.write(fileloc)
        response = HttpResponse(
            s.getvalue(),
            content_type='application/zip'
        )
        response['Content-Disposition'] = 'attachment; filename=' + zip_title
        return response


class AttendanceCreateView(CheckPermissionCreateMixin, AttendanceMixin, OwnerCreateMixin, CreateView):
    template_name = 'reportcard/attendance_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class AttendanceListView(CheckPermissionListMixin, AttendanceMixin, ListView):
    template_name = 'reportcard/attendance_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Teacher'):
            context['attendance'] = Attendance.objects.select_related('grade').prefetch_related('student').\
                filter(created_by=self.request.user)
            return context

        elif self.request.user.groups.filter(name='Admin Assistant') or self.request.user.groups.filter(name='Principal'):
            context['attendance'] = Attendance.objects.select_related('grade').prefetch_related('student')
            return context

        else:
            context['attendance'] = None
            return context


class AttendanceDetailView(CheckPermissionDetailMixin, AttendanceMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Teacher'):
            try:
                attendance = Attendance.objects.select_related('grade').prefetch_related('student').\
                    filter(created_by=self.request.user)
                context['attendance'] = self.get_object(attendance)
                return context
            except Http404:
                raise PermissionDenied

        elif self.request.user.groups.filter(name='Admin Assistant') | self.request.user.groups.filter(name='Principal'):
            attendance = Attendance.objects.select_related('grade').prefetch_related('student')
            context['attendance'] = self.get_object(attendance)
            return context


class AttendanceUpdateView(CheckPermissionUpdateMixin, AttendanceMixin, OwnerMixin, UpdateView):
    template_name = 'reportcard/attendance_update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class AttendanceDeleteView(CheckPermissionDeleteMixin, AttendanceMixin, OwnerMixin, DeleteView):
    template_name = 'reportcard/attendance_delete.html'


class StudentMarksCreateView(CheckPermissionCreateMixin, MarkMixin, OwnerCreateMixin, CreateView):
    template_name = 'reportcard/mark_form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['student_marks'] = StudentMarksFormSet(self.request.POST)
        else:
            data['student_marks'] = StudentMarksFormSet()

        return data

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        context = self.get_context_data()
        student_marks = context['student_marks']

        with transaction.atomic():
            self.object = form.save()
            if student_marks.is_valid():
                student_marks.instance = self.object
                student_marks.created_by = self.request.user
                student_marks.save()
        return super().form_valid(form)


class StudentMarksListView(CheckPermissionListMixin, MarkMixin, QueryMixin, OwnerListMixin, ListView):
    template_name = 'reportcard/mark_list.html'


class StudentMarksUpdateView(MarkMixin, CheckPermissionUpdateMixin, OwnerMixin, UpdateView):

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['student_marks'] = StudentMarksFormSet(self.request.POST, instance=self.object)

        else:
            data['student_marks'] = StudentMarksFormSet(instance=self.object)

        return data

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        context = self.get_context_data()
        student_marks = context['student_marks']

        with transaction.atomic():
            self.object = form.save()
            if student_marks.is_valid():
                student_marks.instance = self.object
                student_marks.created_by = self.object
                student_marks.save()
        return super().form_valid(form)


class StudentMarksDeleteView(CheckPermissionDeleteMixin, MarkMixin, OwnerMixin, DeleteView):
    template_name = 'reportcard/mark_delete.html'


class StudentMarksDetailView(CheckPermissionDetailMixin, MarkMixin, OwnerMixin, DetailView):
    template_name = 'reportcard/mark_detail.html'
