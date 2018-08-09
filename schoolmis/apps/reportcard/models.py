from django.db import models
from django.contrib.auth.models import User

from apps.users.models import StudentProfile, TeacherProfile
from apps.school.models import ExamType


class Subject(models.Model):
    grade = models.ForeignKey('school.grade', related_name='subject_grade')
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, unique=True)
    teacher = models.ForeignKey(TeacherProfile, related_name='subject_teacher', on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('view_subject', 'View Subject'),
        )

    def __str__(self):
        return "Subject:{}".format(self.name)


class Attendance(models.Model):
    created_by = models.ForeignKey(User)
    grade = models.ForeignKey('school.grade', related_name='attendance_grade')
    student = models.ManyToManyField(StudentProfile, related_name='attendance_student')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('view_attendance', 'View Attendance'),
            ('detail_attendance', 'Detail Attendance'),
        )

    def calculate_attendance(self):
        pass

    def get_present_students(self):
        return self.student.all()

    def get_absent_students(self):
        return set(self.grade.student_grade.all()) - set(self.student.all())

    def __str__(self):
        return "Attendance: Grade{}".format(self.grade)


class Mark(models.Model):
    created_by = models.ForeignKey(User, null=True)
    grade = models.ForeignKey('school.grade', related_name='mark_grade')
    subject = models.ForeignKey(Subject, related_name='marks_subjects')
    exam_type = models.ForeignKey(ExamType, related_name='mark_exam_type')
    full_marks = models.DecimalField(max_digits=5, decimal_places=2)
    pass_marks = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        permissions = (
            ('view_mark', 'View Marks'),
            ('detail_mark', 'Detail Marks'),

        )

    def __str__(self):
        return "Grade: {}, Subject: {}".format(self.grade, self.subject.name)


class StudentMarks(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, related_name='studentmarks_mark')
    student = models.ForeignKey('users.studentprofile', related_name='marks_student', on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)


class MarkSheet(models.Model):
    created_by = models.ForeignKey(User)
    grade = models.ForeignKey('school.grade', related_name='marksheet_grade')
    student = models.ForeignKey('users.studentprofile', related_name='marksheet_student')
    exam_type = models.ForeignKey(ExamType, related_name='marksheet_exam_type', null=True)
    issue_date = models.DateField()
    issue_by = models.ForeignKey(TeacherProfile, related_name='issue_by', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('view_marksheet', 'View MarkSheet'),
            ('detail_marksheet', 'Detail MarkSheet')
        )

    def get_total_obtained_marks(self):
        return '{}'.format(sum(mark.marks_obtained for mark in self.student.marks_student.all()))

    def __str__(self):
        return "MarkSheet: {}{}".format(self.student.user.first_name, self.grade)


