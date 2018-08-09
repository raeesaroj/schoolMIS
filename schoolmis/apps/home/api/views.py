from rest_framework.generics import (ListAPIView, CreateAPIView)

from .serializers import (
    TestimonialSerializers, SchoolSerializers, EventSerializers, NoticeSerializers, ContactSerializers)
from apps.home.models import (School, Testimonial, Event, Notice, Contact)


class TestimonialListApiView(ListAPIView):
    queryset = Testimonial.objects.filter(publish=True)
    serializer_class = TestimonialSerializers


class SchoolListApiView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializers


class EventListApiView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializers


class NoticeListApiView(ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializers


class ContactPostApiView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers