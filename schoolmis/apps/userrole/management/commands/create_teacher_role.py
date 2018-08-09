from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Create Teacher Role'

    def handle(self, *args, **options):
        teacher_group, created = Group.objects.get_or_create(name="Teacher")

        # reportCard app
        marksheet_perm = ContentType.objects.get(app_label='reportcard', model='marksheet')
        perms = Permission.objects.filter(content_type=marksheet_perm)
        for p in perms:
            teacher_group.permissions.add(p)

        attendance_perm = ContentType.objects.get(app_label='reportcard', model='attendance')
        perm = Permission.objects.filter(content_type=attendance_perm)
        for p in perm:
            teacher_group.permissions.add(p)

        mark_perm = ContentType.objects.get(app_label='reportcard', model='mark')
        perms = Permission.objects.filter(content_type=mark_perm)
        for p in perms:
            teacher_group.permissions.add(p)

        mark_perm = ContentType.objects.get(app_label='reportcard', model='studentmarks')
        perms = Permission.objects.filter(content_type=mark_perm)
        for p in perms:
            teacher_group.permissions.add(p)

        subject_view_perm = Permission.objects.get(codename='view_subject')
        teacher_group.permissions.add(subject_view_perm)

        # notes app

        assignment_perm = ContentType.objects.get(app_label='notes', model='assignment')
        perm = Permission.objects.filter(content_type=assignment_perm)
        for p in perm:
            teacher_group.permissions.add(p)

        note_perm = ContentType.objects.get(app_label='notes', model='note')
        perm = Permission.objects.filter(content_type=note_perm)
        for p in perm:
            teacher_group.permissions.add(p)

        # school app

        section_view_perm = Permission.objects.get(codename='view_section')
        teacher_group.permissions.add(section_view_perm)

        grade_view_perm = Permission.objects.get(codename='view_grade')
        teacher_group.permissions.add(grade_view_perm)

        grade_detail_perm = Permission.objects.get(codename='detail_grade')
        teacher_group.permissions.add(grade_detail_perm)

        # users app
        teacher_profile_view_perm = Permission.objects.get(codename='view_teacherprofile')
        teacher_group.permissions.add(teacher_profile_view_perm)

        teacher_profile_change_perm = Permission.objects.get(codename='change_teacherprofile')
        teacher_group.permissions.add(teacher_profile_change_perm)

        teacher_profile_detail_perm = Permission.objects.get(codename='detail_teacherprofile')
        teacher_group.permissions.add(teacher_profile_detail_perm)

        student_detail_perm = Permission.objects.get(codename='detail_studentprofile')
        teacher_group.permissions.add(student_detail_perm)

        parent_detail_perm = Permission.objects.get(codename='detail_parentprofile')
        teacher_group.permissions.add(parent_detail_perm)

        self.stdout.write('Successfully created teacher role')