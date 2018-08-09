from django.contrib import admin

from .models import Subject, Attendance, MarkSheet, Mark

admin.site.register(Subject)

admin.site.register(Attendance)

admin.site.register(MarkSheet)

admin.site.register(Mark)