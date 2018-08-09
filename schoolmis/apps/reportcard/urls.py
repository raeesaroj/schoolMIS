from django.conf.urls import url
from .views import (
    SubjectListView,
    AttendanceCreateView,
    AttendanceListView,
    AttendanceDetailView,
    AttendanceUpdateView,
    AttendanceDeleteView,
    MarkSheetCreateView,
    MarkSheetListView,
    MarkSheetDetailView,
    MarkSheetUpdateView,
    MarkSheetDeleteView,
    MarkSheetPdfZipView,
    MarkSheetPdfView,
    StudentMarksCreateView,
    StudentMarksListView,
    StudentMarksDetailView,
    StudentMarksUpdateView,
    StudentMarksDeleteView,
    StudentAutocomplete,


)

urlpatterns = [
    url(r'^subject-list/$', SubjectListView.as_view(), name='subject_list'),

    url(r'^attendance-create/$', AttendanceCreateView.as_view(), name='attendance_create'),
    url(r'^attendance-list/$', AttendanceListView.as_view(), name='attendance_list'),
    url(r'^attendance-detail/(?P<pk>\d+)/$', AttendanceDetailView.as_view(), name='attendance_detail'),
    url(r'^attendance-update/(?P<pk>\d+)/$', AttendanceUpdateView.as_view(), name='attendance_update'),
    url(r'^attendance-delete/(?P<pk>\d+)/$', AttendanceDeleteView.as_view(), name='attendance_delete'),

    url(r'^marksheet-create/$', MarkSheetCreateView.as_view(), name='marksheet_create'),
    url(r'^marksheet-list/$', MarkSheetListView.as_view(), name='marksheet_list'),
    url(r'^marksheet-detail/(?P<pk>\d+)/$', MarkSheetDetailView.as_view(), name='marksheet_detail'),
    url(r'^marksheet-update/(?P<pk>\d+)/$', MarkSheetUpdateView.as_view(), name='marksheet_update'),
    url(r'^marksheet-delete/(?P<pk>\d+)/$', MarkSheetDeleteView.as_view(), name='marksheet_delete'),
    url(r'^marksheet-zip/$', MarkSheetPdfZipView.as_view(), name='marksheet_zip'),
    url(r'^marksheet-pdf/(?P<pk>\d+)/$', MarkSheetPdfView.as_view(), name='marksheet_pdf'),
    url(r'^student-autocomplete/$', StudentAutocomplete.as_view(), name='student_autocomplete'),

    url(r'^mark-create/$', StudentMarksCreateView.as_view(), name='mark_create'),
    url(r'^mark-list/$', StudentMarksListView.as_view(), name='mark_list'),
    url(r'^mark-detail/(?P<pk>\d+)/$', StudentMarksDetailView.as_view(), name='mark_detail'),
    url(r'^mark-update/(?P<pk>\d+)/$', StudentMarksUpdateView.as_view(), name='mark_update'),
    url(r'^mark-delete/(?P<pk>\d+)/$', StudentMarksDeleteView.as_view(), name='mark_delete'),

]
