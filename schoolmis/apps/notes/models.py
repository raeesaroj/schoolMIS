from django.db import models
from django.contrib.auth.models import User

from apps.reportcard.models import Subject
from apps.school.models import Grade
from apps.users.models import StudentProfile


class NoteAssignment(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        abstract = True


class Note(NoteAssignment):
    grade = models.ForeignKey(Grade, related_name='note_grade')
    subject = models.ForeignKey(Subject, related_name='note_subject')
    files = models.FileField(upload_to='notes/', blank=True, null=True)

    class Meta:
        permissions = (
            ('view_note', 'View Note'),
            ('detail_note', 'Detail Note'),

        )

    def __str__(self):
        return "Note: {}, {}".format(self.title, self.subject)


class Assignment(NoteAssignment):
    grade = models.ForeignKey(Grade, related_name='assignment_grade')
    subject = models.ForeignKey(Subject, related_name='assignment_subject')
    student = models.ManyToManyField(StudentProfile)
    files = models.FileField(upload_to='assignment/', blank=True, null=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    submit_date = models.DateTimeField()
    status = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('view_assignment', 'View Assignment'),
            ('detail_assignment', 'Detail Assignment'),
        )

    def __str__(self):
        return "Assignment: {}, {}".format(self.title, self.subject)



