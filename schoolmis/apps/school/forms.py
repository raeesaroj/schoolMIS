from django import forms
from django.forms import inlineformset_factory

from apps.reportcard.models import Subject
from .models import Section, Grade, ExamType


class GradeSubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'


class GradeSectionForm(forms.ModelForm):
    class Meta:
        model = Section
        exclude = ()


GradeSectionFormSet = inlineformset_factory(Grade, Section,
                                            form=GradeSectionForm, extra=1)

GradeSubjectFormSet = inlineformset_factory(Grade, Subject,
                                            form=GradeSubjectForm, extra=1)


class ExamTypeForm(forms.ModelForm):

    class Meta:
        model = ExamType
        fields = '__all__'