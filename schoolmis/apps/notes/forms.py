from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import Note, Assignment
from apps.reportcard.models import Subject
from apps.users.models import StudentProfile
from apps.school.models import Grade


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        exclude = ('created_by',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fields['grade'].queryset = Grade.objects.filter(name__in=user.teacher_profile.subject_teacher.
                                                                 values('grade__name'))
        except ObjectDoesNotExist:
            self.fields['grade'].queryset = Grade.objects.all()

        self.fields['subject'].queryset = Subject.objects.none()

        if 'grade' in self.data:
            try:
                grade_id = int(self.data.get('grade'))
                self.fields['subject'].queryset = Subject.objects.filter(
                    grade_id=grade_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty student queryset
        elif self.instance.pk:
            self.fields['subject'].queryset = self.instance.grade.subject_grade


class AssignmentForm(forms.ModelForm):

    class Meta:
        model = Assignment
        exclude = ('created_by',)

        widgets = {
            'student': forms.CheckboxSelectMultiple(),
        }

        student = forms.ModelMultipleChoiceField(queryset=StudentProfile.objects.all(), required=False)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.fields['grade'].queryset = Grade.objects.filter(name__in=user.teacher_profile.subject_teacher.
                                                                 values('grade__name'))
        except ObjectDoesNotExist:
            self.fields['grade'].queryset = Grade.objects.all()

        self.fields['student'].queryset = StudentProfile.objects.none()
        self.fields['subject'].queryset = Subject.objects.none()

        if 'grade' in self.data:
            try:
                grade_id = int(self.data.get('grade'))
                self.fields['student'].queryset = StudentProfile.objects.filter(
                    grade_id=grade_id)
                self.fields['subject'].queryset = Subject.objects.filter(
                    grade_id=grade_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty student queryset
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.grade.student_grade
            self.fields['subject'].queryset = self.instance.grade.subject_grade
