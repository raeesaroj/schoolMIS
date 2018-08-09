from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Create Guardian Role'

    def handle(self, *args, **options):
        guardian_group, created = Group.objects.get_or_create(name="Guardian")

        # reportCard app
        marksheet_view_perm = Permission.objects.get(codename='view_marksheet')
        guardian_group.permissions.add(marksheet_view_perm)

        marksheet_detail_perm = Permission.objects.get(codename='detail_marksheet')
        guardian_group.permissions.add(marksheet_detail_perm)

        parent_profile_view_perm = Permission.objects.get(codename='view_parentprofile')
        guardian_group.permissions.add(parent_profile_view_perm)

        parent_profile_change_perm = Permission.objects.get(codename='change_parentprofile')
        guardian_group.permissions.add(parent_profile_change_perm)

        parent_profile_detail_perm = Permission.objects.get(codename='detail_parentprofile')
        guardian_group.permissions.add(parent_profile_detail_perm)

        # notes app
        assignment_view_perm = Permission.objects.get(codename='view_assignment')
        guardian_group.permissions.add(assignment_view_perm)

        assignment_detail_perm = Permission.objects.get(codename='detail_assignment')
        guardian_group.permissions.add(assignment_detail_perm)

        note_view_perm = Permission.objects.get(codename='view_note')
        guardian_group.permissions.add(note_view_perm)

        note_detail_perm = Permission.objects.get(codename='detail_note')
        guardian_group.permissions.add(note_detail_perm)

        # school app
        grade_view_perm = Permission.objects.get(codename='view_grade')
        guardian_group.permissions.add(grade_view_perm)

        section_view_perm = Permission.objects.get(codename='view_section')
        guardian_group.permissions.add(section_view_perm)

        # authentication app
        student_detail_perm = Permission.objects.get(codename='detail_studentprofile')
        guardian_group.permissions.add(student_detail_perm)

        self.stdout.write('Successfully created guardian role')