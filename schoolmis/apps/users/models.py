from django.db import models
from django.contrib.auth.models import Group
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.utils.text import slugify

GENDER = (('MALE', 'male'),
          ('FEMALE', 'female'))


class Profile(models.Model):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    gender = models.CharField(max_length=25, choices=GENDER)
    phone = models.CharField(max_length=250, blank=True)
    nationality = CountryField(blank=True)
    temporary_address = models.CharField(max_length=250)
    permanent_address = models.CharField(max_length=250)
    blood_group = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True

    def get_full_name(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.last_name)

    def age_calculate(self):
        pass

    def phone_number(self):
        pass


class ParentProfile(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_profile')
    occupation = models.CharField(max_length=250)
    file = models.ImageField(upload_to='parent/profile/', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    class Meta:
        permissions = (
            ('view_parentprofile', 'View ParentProfile'),
            ('detail_parentprofile', 'Detail ParentProfile'),

        )

    def __str__(self):
        return self.get_full_name()

    def get_childrens(self):
        return self.student_parent.all()


class StudentProfile(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    roll_no = models.CharField(max_length=50, unique=True, blank=True, null=True)
    grade = models.ForeignKey('school.Grade', related_name='student_grade')
    section = models.ForeignKey('school.Section', related_name='student_section', blank=True, null=True)
    joined_date = models.DateField(blank=True, null=True)
    file = models.ImageField(upload_to='student/profile/', null=True, blank=True)
    batch = models.PositiveIntegerField(blank=True, null=True)
    parent = models.ForeignKey(ParentProfile, related_name='student_parent', on_delete=models.CASCADE)
    interest = models.TextField(help_text='example singing,dancing, etc', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    class Meta:
        permissions = (
            ('view_studentprofile', 'View StudentProfile'),
            ('detail_studentprofile', 'Detail StudentProfile'),

        )

    def __str__(self):
        return self.get_full_name()


class TeacherProfile(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    education = models.CharField(max_length=250)
    joined_date = models.DateField(blank=True, null=True)
    file = models.ImageField(upload_to='teacher/profile/', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    class Meta:
        permissions = (
            ('view_teacherprofile', 'View TeacherProfile'),
            ('detail_teacherprofile', 'Detail TeacherProfile'),

        )

    def __str__(self):
        return self.get_full_name()


def delete_user(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()


post_delete.connect(delete_user, sender=StudentProfile)
post_delete.connect(delete_user, sender=TeacherProfile)
post_delete.connect(delete_user, sender=ParentProfile)