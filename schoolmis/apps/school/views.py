from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.db import transaction
from django.core.exceptions import PermissionDenied
from django.http import Http404

from apps.userrole.permissions import CheckPermissionCreateMixin, CheckPermissionListMixin, CheckPermissionUpdateMixin, \
    CheckPermissionDeleteMixin, CheckPermissionDetailMixin
from .forms import GradeSectionFormSet, GradeSubjectFormSet, ExamTypeForm
from .mixins import GradeMixin, ExamTypeMixin
from .models import Grade


class GradeSubjectSectionCreateView(GradeMixin, CheckPermissionCreateMixin, CreateView):

    def get_context_data(self, **kwargs):
        data = super(GradeSubjectSectionCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['grade_section'] = GradeSectionFormSet(self.request.POST)
            data['grade_subject'] = GradeSubjectFormSet(self.request.POST)

        else:
            data['grade_section'] = GradeSectionFormSet()
            data['grade_subject'] = GradeSubjectFormSet()

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        grade_section = context['grade_section']
        grade_subject = context['grade_subject']

        with transaction.atomic():
            self.object = form.save()
            if grade_section.is_valid() and grade_subject.is_valid():
                grade_section.instance = self.object
                grade_subject.instance = self.object
                grade_section.save()
                grade_subject.save()
        return super(GradeSubjectSectionCreateView, self).form_valid(form)


class GradeListView(CheckPermissionListMixin, GradeMixin, ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Student'):
            context['grade'] = Grade.objects.filter(name=self.request.user.student_profile.grade)
            return context
        elif self.request.user.groups.filter(name='Admin Assistant') | self.request.user.groups.filter(name='Principal'):
            try:
                context['grade'] = Grade.objects.all()
                return context
            except TypeError:
                pass
        elif self.request.user.groups.filter(name='Teacher'):
            try:
                context['grade'] = Grade.objects.filter(name__in=self.request.user.teacher_profile.subject_teacher.
                                                        values('grade__name'))
                return context
            except TypeError:
                pass

        else:
            context['grade'] = None
            return context


class GradeDetailView(CheckPermissionDetailMixin, GradeMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Student'):
            try:
                grade = Grade.objects.filter(name=self.request.user.student_profile.grade)
                context['grade'] = self.get_object(grade)
                return context
            except Http404:
                raise PermissionDenied
        elif self.request.user.groups.filter(name='Teacher'):
            try:
                grade = Grade.objects.filter(
                    name__in=self.request.user.teacher_profile.subject_teacher.values('grade__name'))
                context['grade'] = self.get_object(grade)

                return context
            except TypeError:
                pass
        elif self.request.user.groups.filter(name='Admin Assistant') or self.request.user.groups.filter(
                name='Principal'):
            context['grade'] = self.get_object()
            return context
        else:
            context['grade'] = None
            return context


class GradeSubjectSectionUpdateView(GradeMixin, CheckPermissionUpdateMixin, UpdateView):

    def get_context_data(self, **kwargs):
        data = super(GradeSubjectSectionUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['grade_section'] = GradeSectionFormSet(self.request.POST, instance=self.object)
            data['grade_subject'] = GradeSubjectFormSet(self.request.POST, instance=self.object)

        else:
            data['grade_section'] = GradeSectionFormSet(instance=self.object)
            data['grade_subject'] = GradeSubjectFormSet(instance=self.object)

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        grade_section = context['grade_section']
        grade_subject = context['grade_subject']

        with transaction.atomic():
            self.object = form.save()

            if grade_section.is_valid() and grade_subject.is_valid():
                grade_section.instance = self.object
                grade_subject.instance = self.object

                grade_section.save()
                grade_subject.save()
        return super(GradeSubjectSectionUpdateView, self).form_valid(form)


class GradeDeleteView(GradeMixin, CheckPermissionDeleteMixin, DeleteView):
    template_name = 'school/grade_delete.html'


class ExamTypeCreateView(ExamTypeMixin, CheckPermissionCreateMixin, CreateView):
    pass


class ExamTypeListView(ExamTypeMixin, CheckPermissionListMixin, ListView):
    pass


class ExamTypeUpdateView(ExamTypeMixin, CheckPermissionUpdateMixin, UpdateView):
    pass


class ExamTypeDeleteView(ExamTypeMixin, CheckPermissionDeleteMixin, DeleteView):
    template_name = 'school/examtype_delete.html'