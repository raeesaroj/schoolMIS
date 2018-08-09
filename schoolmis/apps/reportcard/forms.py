from django import forms
from django.forms import inlineformset_factory

from dal import autocomplete
from decimal import Decimal

from apps.school.models import Grade
from apps.users.models import StudentProfile
from .models import Subject, Attendance, MarkSheet, Mark, StudentMarks


class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        exclude = ('created_by', 'slug',)

        widgets = {
            'student': forms.CheckboxSelectMultiple()
        }

        student = forms.ModelMultipleChoiceField(queryset=StudentProfile.objects.all(), required=False)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].queryset = Grade.objects.filter(name__in=user.teacher_profile.class_teacher.values('grade__name'))
        self.fields['student'].queryset = StudentProfile.objects.none()

        if 'grade' in self.data:
            try:
                grade_id = int(self.data.get('grade'))
                self.fields['student'].queryset = StudentProfile.objects.filter(grade_id=grade_id)

            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty student queryset
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.grade.student_grade


class MarkSheetForm(forms.ModelForm):

    class Meta:
        model = MarkSheet
        fields = ('grade', 'student', 'exam_type', 'issue_by', 'issue_date', 'publish')
        widgets = {
            'student': autocomplete.ModelSelect2(url='reportcard:student_autocomplete', forward=['grade'])
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].queryset = Grade.objects.filter(name__in=user.teacher_profile.class_teacher.
                                                             values('grade__name'))
        self.fields['student'].queryset = StudentProfile.objects.none()

        if 'grade' in self.data:
            try:
                grade_id = int(self.data.get('grade'))
                self.fields['student'].queryset = StudentProfile.objects.filter(grade_id=grade_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty student queryset
        elif self.instance.pk:
            self.fields['student'].queryset = self.instance.grade.student_grade


class StudentMarksForm(forms.ModelForm):

    class Meta:
        model = StudentMarks
        fields = '__all__'

    # def clean_marks_obtained(self):
    #     full_marks = self.data.get('full_marks')
    #     marks_obtained = self.cleaned_data['marks_obtained']
    #     if marks_obtained > Decimal(full_marks):
    #         raise forms.ValidationError('Marks obtained must not be greater than Full marks')


StudentMarksFormSet = inlineformset_factory(Mark, StudentMarks,
                                            form=StudentMarksForm, extra=0)


class MarkForm(forms.ModelForm):

    class Meta:
        model = Mark
        exclude = ('created_by',)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grade'].queryset = Grade.objects.filter(name__in=user.teacher_profile.subject_teacher.
                                                             values('grade__name'))
        self.fields['subject'].queryset = Subject.objects.none()

        if 'grade' in self.data:
            try:
                grade_id = int(self.data.get('grade'))
                self.fields['subject'].queryset = Subject.objects.filter(
                        grade_id=grade_id, teacher=user.teacher_profile)

            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty student queryset
        elif self.instance.pk:
            self.fields['subject'].queryset = self.instance.grade.subject_grade

    def clean_pass_marks(self):
        pass_marks = self.cleaned_data['pass_marks']
        full_marks = Decimal(self.data.get('full_marks'))
        if pass_marks >= full_marks:
            raise forms.ValidationError('Pass marks must be less than full marks')
        return pass_marks