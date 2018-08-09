from django.conf.urls import url
from .views import (
    NoteCreateView,
    NoteListView,
    NoteDetailView,
    NoteUpdateView,
    NoteDeleteView,
    AssignmentCreateView,
    AssignmentListView,
    AssignmentDetailView,
    AssignmentUpdateView,
    AssignmentDeleteView,
    load_students_subjects,
    load_students_subjects_formset,
    load_subjects,
    load_students,



)
urlpatterns = [

    url(r'^note-create/$', NoteCreateView.as_view(), name='note_create'),
    url(r'^note-list/$', NoteListView.as_view(), name='note_list'),
    url(r'^note-detail/(?P<pk>\d+)/$', NoteDetailView.as_view(), name='note_detail'),
    url(r'^note-update/(?P<pk>\d+)/$', NoteUpdateView.as_view(), name='note_update'),
    url(r'^note-delete/(?P<pk>\d+)/$', NoteDeleteView.as_view(), name='note_delete'),

    url(r'^assignment-create/$', AssignmentCreateView.as_view(), name='assignment_create'),
    url(r'^assignment-list/$', AssignmentListView.as_view(), name='assignment_list'),
    url(r'^assignment-detail/(?P<pk>\d+)/$', AssignmentDetailView.as_view(), name='assignment_detail'),
    url(r'^assignment-update/(?P<pk>\d+)/$', AssignmentUpdateView.as_view(), name='assignment_update'),
    url(r'^assignment-delete/(?P<pk>\d+)/$', AssignmentDeleteView.as_view(), name='assignment_delete'),
    url('ajax/load-students-subjects/', load_students_subjects, name='ajax_load_students_subjects'),
    url('ajax/load-students-subjects-formset/', load_students_subjects_formset, name='ajax_load_students_subjects_formset'),
    url('ajax/load-subjects/', load_subjects, name='ajax_load_subjects'),
    url('ajax/load-students/', load_students, name='ajax_load_students'),

]