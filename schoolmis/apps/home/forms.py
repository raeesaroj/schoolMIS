from django import forms

from .models import School, Testimonial, Event, Notice


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = '__all__'


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = '__all__'


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'


class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = '__all__'
