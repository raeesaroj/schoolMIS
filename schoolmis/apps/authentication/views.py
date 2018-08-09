from django.shortcuts import redirect, render, reverse, Http404
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import Group
from django.db.models import Q
from django.core.exceptions import PermissionDenied

from dal import autocomplete

from apps.users.models import ParentProfile, StudentProfile, TeacherProfile
from apps.userrole.permissions import CheckPermissionCreateMixin, CheckPermissionUpdateMixin, CheckPermissionListMixin, \
    CheckPermissionDeleteMixin, CheckPermissionDetailMixin
from .forms import TeacherSignupForm, ParentSignupForm, StudentSignupForm, StudentForm, ParentForm, TeacherForm
from .mixins import TeacherMixin, StudentMixin, ParentMixin

from .resources import ParentResource, StudentResource, TeacherResource


class ParentAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = ParentProfile.objects.all()

        if self.q:
            qs = qs.filter(Q(first_name__icontains=self.q) | Q(last_name__icontains=self.q))
        return qs


class TeacherCreateView(CheckPermissionCreateMixin, TeacherMixin, CreateView):
    template_name = 'authentication/teacherprofile_form.html'

    def get(self, request, *args, **kwargs):
        form = TeacherSignupForm(initial={'nationality': 'NP'})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TeacherSignupForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            user.groups.add(Group.objects.get(name='Teacher'))

            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            temporary_address = form.cleaned_data['temporary_address']
            permanent_address = form.cleaned_data['permanent_address']
            nationality = form.cleaned_data['nationality']
            education = form.cleaned_data['education']
            TeacherProfile.objects.create(user=user, first_name=first_name, middle_name=middle_name,
                                          last_name=last_name, email=email, gender=gender, phone=phone,
                                          temporary_address=temporary_address, permanent_address=permanent_address,
                                          education=education, nationality=nationality)
            return redirect('authentication:teacher_list')

        return render(request, self.template_name, {'form': form})


class TeacherListView(CheckPermissionListMixin, TeacherMixin, ListView):
    template_name = 'authentication/teacherprofile_list.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            if self.request.user.groups.filter(name='Teacher'):
                context['teacher'] = TeacherProfile.objects.filter(user=self.request.user)
                return context
            else:
                context['teacher'] = TeacherProfile.objects.all()
                return context
        except:
            pass


class TeacherDetailView(CheckPermissionDetailMixin, TeacherMixin, DetailView):
    template_name = 'authentication/teacherprofile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Teacher'):
            try:
                teacher = TeacherProfile.objects.filter(user=self.request.user)
                context['teacher'] = self.get_object(teacher)
                return context
            except Http404:
                raise PermissionDenied

        else:
            context['teacher'] = self.get_object()
            return context


class TeacherUpdateView(SuccessMessageMixin, CheckPermissionUpdateMixin, UpdateView):
    form_class = TeacherForm
    model = TeacherProfile
    template_name = 'authentication/teacherprofile_update.html'
    success_message = "Profile Updated Successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Teacher'):
            try:
                teacher = TeacherProfile.objects.filter(user=self.request.user)
                context['teacher'] = self.get_object(teacher)
                return context
            except Http404:
                raise PermissionDenied

        else:
            context['teacher'] = self.get_object()
            return context

    def get_success_url(self):
        return reverse('authentication:teacher_update', kwargs={'slug': self.object.slug})


class TeacherDeleteView(CheckPermissionDeleteMixin, TeacherMixin, DeleteView):
    template_name = 'authentication/teacherprofile_delete.html'


class StudentCreateView(CheckPermissionCreateMixin, StudentMixin, CreateView):
    template_name = 'authentication/studentprofile_form.html'

    def get(self, request, *args, **kwargs):
        form = StudentSignupForm(initial={'nationality': 'NP'})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            user.groups.add(Group.objects.get(name='Student'))

            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            temporary_address = form.cleaned_data['temporary_address']
            permanent_address = form.cleaned_data['permanent_address']
            nationality = form.cleaned_data['nationality']
            grade = form.cleaned_data['grade']
            parent = form.cleaned_data['parent']

            StudentProfile.objects.create(user=user, first_name=first_name, middle_name=middle_name, email=email,
                                          last_name=last_name, gender=gender, phone=phone,
                                          temporary_address=temporary_address, permanent_address=permanent_address,
                                          grade=grade, parent=parent, nationality=nationality)
            return redirect('authentication:student_list')

        return render(request, self.template_name, {'form': form})


class StudentListView(CheckPermissionListMixin, StudentMixin, ListView):
    template_name = 'authentication/studentprofile_list.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            if self.request.user.groups.filter(name='Student'):
                context['students'] = StudentProfile.objects.filter(user=self.request.user)
                return context
            else:
                context['students'] = StudentProfile.objects.all()
                return context
        except:
            pass


class StudentDetailView(CheckPermissionDetailMixin, StudentMixin, DetailView):
    template_name = 'authentication/studentprofile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Student'):
            try:
                students = StudentProfile.objects.filter(user=self.request.user)
                context['students'] = self.get_object(students)
                return context
            except Http404:
                raise PermissionDenied

        else:
            context['students'] = self.get_object()
            return context


class StudentUpdateView(SuccessMessageMixin, CheckPermissionUpdateMixin, UpdateView):
    form_class = StudentForm
    model = StudentProfile
    template_name = 'authentication/studentprofile_update.html'
    success_message = "Profile Updated Successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Student'):
            try:
                students = StudentProfile.objects.filter(user=self.request.user)
                context['students'] = self.get_object(students)
                return context
            except Http404:
                raise PermissionDenied

        else:
            context['students'] = self.get_object()
            return context

    def get_success_url(self):
        return reverse('authentication:student_update', kwargs={'slug': self.object.slug})


class StudentDeleteView(CheckPermissionDeleteMixin, StudentMixin, DeleteView):
    template_name = 'authentication/studentprofile_delete.html'


class ParentCreateView(CheckPermissionCreateMixin, ParentMixin, CreateView):
    template_name = 'authentication/parentprofile_form.html'

    def get(self, request, *args, **kwargs):
        form = ParentSignupForm(initial={'nationality': 'NP'})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            user.groups.add(Group.objects.get(name='Guardian'))

            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            temporary_address = form.cleaned_data['temporary_address']
            permanent_address = form.cleaned_data['permanent_address']
            nationality = form.cleaned_data['nationality']
            occupation = form.cleaned_data['occupation']

            ParentProfile.objects.create(user=user, first_name=first_name, middle_name=middle_name, last_name=last_name,
                                         email=email, gender=gender, phone=phone, temporary_address=temporary_address,
                                         permanent_address=permanent_address, occupation=occupation,
                                         nationality=nationality)
            return redirect('authentication:parent_list')

        return render(request, self.template_name, {'form': form})


class ParentListView(CheckPermissionListMixin, ParentMixin, ListView):
    template_name = 'authentication/parentprofile_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.groups.filter(name='Guardian'):
            context['parent'] = ParentProfile.objects.filter(user=self.request.user)
            return context
        else:
            context['parent'] = ParentProfile.objects.all()
            return context


class ParentDetailView(CheckPermissionDetailMixin, ParentMixin, DetailView):
    template_name = 'authentication/parentprofile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Guardian'):
            try:
                parent = ParentProfile.objects.filter(user=self.request.user)
                context['parent'] = self.get_object(parent)
                return context
            except Http404:
                raise PermissionDenied

        else:
            context['parent'] = self.get_object()
            return context


class ParentUpdateView(SuccessMessageMixin, CheckPermissionUpdateMixin, UpdateView):
    form_class = ParentForm
    model = ParentProfile
    template_name = 'authentication/parentprofile_update.html'
    success_message = "Profile Updated Successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.groups.filter(name='Guardian'):
            try:
                parent = ParentProfile.objects.filter(user=self.request.user)
                context['parent'] = self.get_object(parent)
                return context
            except Http404:
                raise PermissionDenied

        else:
            context['parent'] = self.get_object()
            return context

    def get_success_url(self):
        return reverse('authentication:parent_update', kwargs={'slug': self.object.slug})


class ParentDeleteView(CheckPermissionDeleteMixin, ParentMixin, DeleteView):
    template_name = 'authentication/parentprofile_delete.html'



# Exporting to Excel view
def export_parent(request):
    parent_resource = ParentResource()
    dataset = parent_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="parent_list.xls"'
    return response


def export_student(request, slug):
    student_resource = StudentResource()
    student_list_by_grade = StudentProfile.objects.filter(grade__name = slug)
    dataset = student_resource.export(queryset = student_list_by_grade)
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    filename = "student_list_grade_{}".format(slug) + ".xls"
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return response


def export_teacher(request):
    teacher_resource = TeacherResource()
    dataset = teacher_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="teacher_list.xls"'
    return response
