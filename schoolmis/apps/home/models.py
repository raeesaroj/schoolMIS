from django.db import models
from django.utils import timezone


class School(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=300)
    pan_no = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return "School: {}".format(self.name)


class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    message = models.CharField(max_length=1500)
    image = models.FileField(upload_to='Testimonial')
    publish = models.BooleanField(default=False)

    def __str__(self):
        return "Testimonial: {}".format(self.name)


class Event(models.Model):
    title = models.CharField(max_length=250)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        permissions = (
            ('view_event', 'View Events'),
            ('detail_event', 'Detail Events'),

        )

    @staticmethod
    def get_status(self):
        now = timezone.now()
        date = self.day
        if now <= date:
            self.status = True  # if status is true event is upcoming
        else:
            self.status = False  # if status is false event is past
        self.save()
        return self.status


class Notice(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField(help_text="write description about notice")
    date = models.DateField(help_text="when ?")
    time = models.TimeField()

    def __str__(self):
        return self.title

    class Meta:
        permissions = (
            ('view_notice', 'View Notices'),
            ('detail_notice', 'Detail Notices'),

        )


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'name:{}-email'.format(self.name, self.email)
