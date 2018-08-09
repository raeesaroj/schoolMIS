from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Create Student Role'

    def handle(self, *args, **options):
        student_group, created = Group.objects.get_or_create(name="Student")

        # reportCard app
        marksheet_view_perm = Permission.objects.get(codename='view_marksheet')
        student_group.permissions.add(marksheet_view_perm)

        marksheet_detail_perm = Permission.objects.get(codename='detail_marksheet')
        student_group.permissions.add(marksheet_detail_perm)

        subject_view_perm = Permission.objects.get(codename='view_subject')
        student_group.permissions.add(subject_view_perm)

        subject_view_perm = Permission.objects.get(codename='view_subject')
        student_group.permissions.add(subject_view_perm)

        # notes app
        assignment_view_perm = Permission.objects.get(codename='view_assignment')
        student_group.permissions.add(assignment_view_perm)

        assignment_detail_perm = Permission.objects.get(codename='detail_assignment')
        student_group.permissions.add(assignment_detail_perm)

        note_view_perm = Permission.objects.get(codename='view_note')
        student_group.permissions.add(note_view_perm)

        note_detail_perm = Permission.objects.get(codename='detail_note')
        student_group.permissions.add(note_detail_perm)

        # school app

        section_view_perm = Permission.objects.get(codename='view_section')
        student_group.permissions.add(section_view_perm)

        grade_view_perm = Permission.objects.get(codename='view_grade')
        student_group.permissions.add(grade_view_perm)

        grade_detail_perm = Permission.objects.get(codename='detail_grade')
        student_group.permissions.add(grade_detail_perm)

        # users app
        student_profile_view_perm = Permission.objects.get(codename='view_studentprofile')
        student_group.permissions.add(student_profile_view_perm)

        student_profile_change_perm = Permission.objects.get(codename='change_studentprofile')
        student_group.permissions.add(student_profile_change_perm)

        student_profile_detail_perm = Permission.objects.get(codename='detail_studentprofile')
        student_group.permissions.add(student_profile_detail_perm)

        self.stdout.write('Successfully created student role')