from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from apps.home.models import School, Testimonial, Event, Notice, Contact


class SchoolSerializers(ModelSerializer):

    class Meta:
        model = School
        fields = "__all__"


class TestimonialSerializers(ModelSerializer):

    class Meta:
        model = Testimonial
        fields = "__all__"


class EventSerializers(ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"


class NoticeSerializers(ModelSerializer):

    class Meta:
        model = Notice
        fields = "__all__"


class ContactSerializers(ModelSerializer):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message',)