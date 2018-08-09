from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.template.loader import render_to_string
from django.core.exceptions import PermissionDenied

from apps.userrole.permissions import CheckPermissionCreateMixin, CheckPermissionUpdateMixin, \
    CheckPermissionDeleteMixin, CheckPermissionDetailMixin, CheckPermissionListMixin
from libs.views_mixins_utils import QueryMixin, OwnerMixin, OwnerCreateMixin
from apps.reportcard.models import Subject
from apps.users.models import StudentProfile
from .models import Note, Assignment
from .mixins import NoteMixin, AssignmentMixin


class NoteCreateView(CheckPermissionCreateMixin, NoteMixin, OwnerCreateMixin, CreateView):
    template_name = 'notes/note_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class NoteListView(CheckPermissionListMixin, NoteMixin, ListView):
    template_name = 'notes/note_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if self.request.user.groups.filter(name='Student'):
                context['note'] = Note.objects.select_related().filter(
                    grade=self.request.user.student_profile.grade)
                return context
            elif self.request.user.groups.filter(name='Teacher') | self.request.user.groups.filter(
                    name='Admin Assistant'):
                try:
                    context['note'] = Note.objects.select_related().filter(created_by=self.request.user)
                    return context
                except TypeError:
                    pass
            elif self.request.user.groups.filter(name='Guardian'):
                try:
                    context['note'] = Note.objects.select_related().filter(
                            grade__name__in=self.request.user.parent_profile.student_parent.values('grade__name'))
                    return context
                except TypeError:
                    pass

            else:
                try:
                    context['note'] = None
                    return context
                except TypeError:
                    pass

        except StudentProfile.DoesNotExist:
            pass


class NoteDetailView(CheckPermissionDetailMixin, NoteMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Student'):
            try:
                note = Note.objects.filter(
                    grade=self.request.user.student_profile.grade)
                context['note'] = self.get_object(note)
                return context
            except Http404:
                raise PermissionDenied
        elif self.request.user.groups.filter(name='Guardian'):
            try:
                note = Note.objects.select_related().filter(
                            grade__name__in=self.request.user.parent_profile.student_parent.values('grade__name'))
                context['note'] = self.get_object(note)
                return context
            except Http404:
                raise PermissionDenied

        else:
            context['note'] = self.get_object()
            if context['note'].created_by != self.request.user:
                raise PermissionDenied
            return context


class NoteUpdateView(CheckPermissionUpdateMixin, NoteMixin, OwnerMixin, UpdateView):
    template_name = 'notes/note_update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class NoteDeleteView(CheckPermissionDeleteMixin, NoteMixin, OwnerMixin, DeleteView):
    template_name = 'notes/note_delete.html'


class AssignmentCreateView(CheckPermissionCreateMixin, AssignmentMixin, OwnerCreateMixin, CreateView):
    template_name = 'notes/assignment_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class AssignmentListView(AssignmentMixin, QueryMixin, ListView):
    template_name = 'notes/assignment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            if self.request.user.groups.filter(name='Student'):
                context['assignment'] = Assignment.objects.select_related().\
                    filter(student=self.request.user.student_profile)
                return context
            elif self.request.user.groups.filter(name='Teacher') | self.request.user.groups.filter(
                    name='Admin Assistant'):
                try:
                    context['assignment'] = Assignment.objects.select_related().filter(created_by=self.request.user)
                    return context
                except TypeError:
                    pass
            elif self.request.user.groups.filter(name='Guardian'):
                try:
                    context['assignment'] = Assignment.objects.select_related().filter(
                            student__in=self.request.user.parent_profile.student_parent.all())
                    return context
                except:
                    pass

            else:
                try:
                    context['assignment'] = None
                    return context
                except TypeError:
                    pass

        except StudentProfile.DoesNotExist:
            pass


class AssignmentDetailView(AssignmentMixin, DetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Student'):
            try:
                assignment = Assignment.objects.filter(
                    student=self.request.user.student_profile)
                context['assignment'] = self.get_object(assignment)
                return context
            except Http404:
                raise PermissionDenied

        elif self.request.user.groups.filter(name='Guardian'):
            try:
                assignment = Assignment.objects.filter(
                    student__in=self.request.user.parent_profile.student_parent.all())
                context['assignment'] = self.get_object(assignment)
                return context
            except Assignment.MultipleObjectsReturned:
                assignment = Assignment.objects.filter(
                       pk=self.kwargs['pk'])
                context['assignment'] = self.get_object(assignment)
                return context
        else:
            context['assignment'] = self.get_object()
            if context['assignment'].created_by != self.request.user:
                raise PermissionDenied
            return context


class AssignmentUpdateView(CheckPermissionUpdateMixin, AssignmentMixin, OwnerMixin, UpdateView):
    template_name = 'notes/assignment_update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class AssignmentDeleteView(CheckPermissionDeleteMixin, AssignmentMixin, OwnerMixin, DeleteView):
    template_name = 'notes/assignment_delete.html'


def load_students_subjects(request):
    grade = request.GET.get('grade')
    students = StudentProfile.objects.filter(grade=grade)
    students_data = {'students': students}
    str_students = render_to_string(
        'notes/student_dropdown_list_options.html', students_data)
    subjects = Subject.objects.filter(grade=grade)
    subjects_data = {'subjects': subjects}
    str_subjects = render_to_string(
        'notes/subject_dropdown_list_options.html', subjects_data)
    response_data = {'students': str_students, 'subjects': str_subjects}
    return JsonResponse(response_data)


def load_students_subjects_formset(request):
    grade = request.GET.get('grade')
    students = StudentProfile.objects.filter(grade=grade)
    students_data = {'students': students}
    str_students = render_to_string(
        'notes/student_dropdown_formset.html', students_data)
    subjects = Subject.objects.filter(grade=grade, teacher=request.user.teacher_profile)
    subjects_data = {'subjects': subjects}
    str_subjects = render_to_string(
        'notes/subject_dropdown_list_options.html', subjects_data)
    response_data = {'students': str_students, 'subjects': str_subjects}
    return JsonResponse(response_data)


def load_subjects(request):
    grade = request.GET.get('grade')
    subject = Subject.objects.filter(grade=grade)
    return render(request, 'notes/subject_dropdown_list_options.html', {'subjects': subject})


def load_students(request):
    grade = request.GET.get('grade')
    students = StudentProfile.objects.filter(grade=grade)
    return render(request, 'notes/student_note_dropdown_list_options.html', {'students': students})
