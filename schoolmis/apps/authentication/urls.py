from django.conf.urls import url
from django.contrib.auth import views as auth_views
from apps.authentication import views
from schoolmis.decorators import anonymous_required

from .views import (
    TeacherCreateView,
    TeacherListView,
    TeacherDetailView,
    TeacherUpdateView,
    TeacherDeleteView,
    StudentCreateView,
    StudentListView,
    StudentDetailView,
    StudentUpdateView,
    StudentDeleteView,
    ParentCreateView,
    ParentListView,
    ParentDetailView,
    ParentUpdateView,
    ParentDeleteView,
    ParentAutocomplete,
    export_parent,
    export_student,
    export_teacher,

    )

urlpatterns = [	
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', anonymous_required(auth_views.login), {'template_name': 'registration/signin.html'},
        name='login'),

    url(r'^teacher-create/$', TeacherCreateView.as_view(), name='teacher_create'),
    url(r'^teacher-list/$', TeacherListView.as_view(), name='teacher_list'),
    url(r'^teacher-detail/(?P<slug>[\w-]+)/$', TeacherDetailView.as_view(), name='teacher_detail'),
    url(r'^teacher-update/(?P<slug>[\w-]+)/$', TeacherUpdateView.as_view(), name='teacher_update'),
    url(r'^teacher-delete/(?P<slug>[\w-]+)/$', TeacherDeleteView.as_view(), name='teacher_delete'),

    url(r'^student-create/$', StudentCreateView.as_view(), name='student_create'),
    url(r'^student-list/$', StudentListView.as_view(), name='student_list'),
    url(r'^student-detail/(?P<slug>[\w-]+)/$', StudentDetailView.as_view(), name='student_detail'),
    url(r'^student-update/(?P<slug>[\w-]+)/$', StudentUpdateView.as_view(), name='student_update'),
    url(r'^student-delete/(?P<slug>[\w-]+)/$', StudentDeleteView.as_view(), name='student_delete'),

    url(r'^parent-create/$', ParentCreateView.as_view(), name='parent_create'),
    url(r'^parent-list/$', ParentListView.as_view(), name='parent_list'),
    url(r'^parent-detail/(?P<slug>[\w-]+)/$', ParentDetailView.as_view(), name='parent_detail'),
    url(r'^parent-update/(?P<slug>[\w-]+)/$', ParentUpdateView.as_view(), name='parent_update'),
    url(r'^parent-delete/(?P<slug>[\w-]+)/$', ParentDeleteView.as_view(), name='parent_delete'),
    url(r'^parent-autocomplete/$', ParentAutocomplete.as_view(), name='parent_autocomplete'),
    url(r'^export-parent/$', export_parent, name='export-parent'),
    url(r'^export-student/(?P<slug>[\w-]+)/$', export_student, name='export-student'),
    url(r'^export-teacher/$', export_teacher, name='export-teacher'),

]