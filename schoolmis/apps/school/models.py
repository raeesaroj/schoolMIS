from django.db import models
from apps.users.models import TeacherProfile
from django.utils.text import slugify


class ExamType(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ('view_examtype', 'View ExamType'),

        )


class Grade(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        permissions = (
            ('view_grade', 'View Grade'),
            ('detail_grade', 'Detail Grade'),

        )

    def __str__(self):
        return self.name

    def get_section(self):
        return "section: {}".format(self.section_set.all().values('name', 'class_teacher__user__first_name'))

    def get_subjects(self):
        return "subjects: {}".format(self.subject_grade.all().values('name', 'code', 'teacher__user__first_name'))

    def get_students(self):
        return "students: {}".format(self.student_grade.all())


class Section(models.Model):
    name = models.CharField(max_length=15, default='A')
    grade = models.ForeignKey(Grade)
    class_teacher = models.ForeignKey(TeacherProfile, related_name='class_teacher', on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('view_section', 'View Section'),
        )

    def __str__(self):
        return self.name