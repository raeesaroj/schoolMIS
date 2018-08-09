from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView

from apps.userrole import permissions
from .mixins import SchoolMixin, TestimonialMixin, EventMixin, NoticeMixin
from .models import Event, Notice


class HomeView(TemplateView):
    template_name = 'home/home.html'


class SchoolCreateView(permissions.CheckPermissionListMixin,SchoolMixin, CreateView):
    template_name = 'home/school_form.html'


class SchoolListView(TestimonialMixin, ListView):
    template_name = 'home/school_list.html'


class SchoolUpdateView(permissions.CheckPermissionUpdateMixin, SchoolMixin, UpdateView):
    template_name = 'home/school_update.html'


class SchoolDeleteView(permissions.CheckPermissionDeleteMixin, SchoolMixin, DeleteView):
    template_name = 'home/school_delete.html'


class TestimonialCreateView(permissions.CheckPermissionListMixin,TestimonialMixin, CreateView):
    template_name = 'home/testimonial_form.html'


class TestimonialListView(TestimonialMixin, ListView):
    template_name = 'home/testimonial_list.html'


class TestimonialUpdateView(permissions.CheckPermissionUpdateMixin, TestimonialMixin, UpdateView):
    template_name = 'home/testimonial_update.html'


class TestimonialDeleteView(permissions.CheckPermissionDeleteMixin, TestimonialMixin, DeleteView):
    template_name = 'home/testimonial_delete.html'


class EventCreateView(permissions.CheckPermissionCreateMixin, EventMixin, CreateView):
    pass


class EventListView(EventMixin, ListView):

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['events'] = Event.objects.all()
            return context
        except:
            pass


class EventDetailView(EventMixin, DetailView):
    pass


class EventUpdateView(permissions.CheckPermissionUpdateMixin, EventMixin, UpdateView):
    pass


class EventDeleteView(permissions.CheckPermissionDeleteMixin, EventMixin, DeleteView):
    template_name = 'home/event_delete.html'


class NoticeCreateView(permissions.CheckPermissionCreateMixin, NoticeMixin, CreateView):
    pass


class NoticeListView(NoticeMixin, ListView):

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['notices'] = Notice.objects.all()
            return context
        except:
            pass


class NoticeDetailView(NoticeMixin, DetailView):
    pass


class NoticeUpdateView(permissions.CheckPermissionUpdateMixin, NoticeMixin, UpdateView):
    pass


class NoticeDeleteView(permissions.CheckPermissionDeleteMixin, NoticeMixin, DeleteView):
    template_name = 'home/notice_delete.html'
