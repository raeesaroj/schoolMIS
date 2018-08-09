from django.shortcuts import reverse

from .models import School, Testimonial, Event, Notice
from .forms import SchoolForm, TestimonialForm, EventForm, NoticeForm


class SchoolMixin(object):
    model = School
    form_class = SchoolForm
    context_object_name = 'school'


class TestimonialMixin(object):
    model = Testimonial
    form_class = TestimonialForm
    context_object_name = 'testimonial'


class EventMixin(object):
    model = Event
    form_class = EventForm
    context_object_name = 'events'

    def get_success_url(self):
        return reverse('home:event_list')


class NoticeMixin(object):
    model = Notice
    form_class = NoticeForm
    context_object_name = 'notices'

    def get_success_url(self):
        return reverse('home:notice_list')