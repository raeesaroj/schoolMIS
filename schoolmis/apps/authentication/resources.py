from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from apps.users.models import ParentProfile, StudentProfile, TeacherProfile
from apps.school.models import Grade, Section


class ParentResource(resources.ModelResource):
    username = fields.Field(
        column_name='username',
        attribute='user',
        widget=(ForeignKeyWidget(User, 'username'))
    )

    class Meta:
        model = ParentProfile
        exclude = ('user', 'id', 'image', )


class StudentResource(resources.ModelResource):
    username = fields.Field(
        column_name='username',
        attribute='user',
        widget=(ForeignKeyWidget(User, 'username'))
    )
    grade = fields.Field(
        column_name='grade',
        attribute='grade',
        widget=(ForeignKeyWidget(Grade, 'name'))
    )
    section = fields.Field(
        column_name='section',
        attribute='section',
        widget=(ForeignKeyWidget(Section, 'name'))
    )
    parent = fields.Field(
        column_name='parent',
        attribute='parent',
        widget=(ForeignKeyWidget(ParentProfile, 'first_name'))
    )

    class Meta:
        model = StudentProfile
        exclude = ('user', 'grade', 'section', 'parent', 'slug', 'id', 'file', )


class TeacherResource(resources.ModelResource):
    username = fields.Field(
        column_name='username',
        attribute='user',
        widget=(ForeignKeyWidget(User, 'username'))
    )

    class Meta:
        model = TeacherProfile
        exclude = ('user', 'id', 'slug', 'image', )