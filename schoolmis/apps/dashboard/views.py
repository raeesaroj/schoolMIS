from apps.reportcard.views import MarkSheetListView, AttendanceListView
from apps.authentication.views import StudentListView, ParentListView, TeacherListView
from apps.school.views import GradeListView
from apps.home.views import EventListView, NoticeListView
from apps.notes.views import NoteListView, AssignmentListView


class Dashboard(NoteListView, AssignmentListView,  StudentListView, TeacherListView, GradeListView, EventListView,
                NoticeListView, MarkSheetListView, ParentListView, AttendanceListView):
    template_name = 'dashboard/dashboard.html'
