from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    help = 'Create Admin Assistant Role'

    def handle(self, *args, **options):
        admin_assistant, created = Group.objects.get_or_create(name="Admin Assistant")

        # home app
        events = ContentType.objects.get(app_label='home', model='event')
        perms = Permission.objects.filter(content_type=events)
        for p in perms:
            admin_assistant.permissions.add(p)

        contact = ContentType.objects.get(app_label='home', model='contact')
        perms = Permission.objects.filter(content_type=contact)
        for p in perms:
            admin_assistant.permissions.add(p)

        notices = ContentType.objects.get(app_label='home', model='notice')
        perms = Permission.objects.filter(content_type=notices)
        for p in perms:
            admin_assistant.permissions.add(p)

        school = ContentType.objects.get(app_label='home', model='school')
        perms = Permission.objects.filter(content_type=school)
        for p in perms:
            admin_assistant.permissions.add(p)

        testimonial = ContentType.objects.get(app_label='home', model='testimonial')
        perms = Permission.objects.filter(content_type=testimonial)
        for p in perms:
            admin_assistant.permissions.add(p)

        # reportCard app
        subject_perm = ContentType.objects.get(app_label='reportcard', model='subject')
        perms = Permission.objects.filter(content_type=subject_perm)
        for p in perms:
            admin_assistant.permissions.add(p)

        attendance_view_perm = Permission.objects.get(codename='view_attendance')
        admin_assistant.permissions.add(attendance_view_perm)

        attendance_detail_perm = Permission.objects.get(codename='detail_attendance')
        admin_assistant.permissions.add(attendance_detail_perm)

        # notes app
        assignment_perm = ContentType.objects.get(app_label='notes', model='assignment')
        perm = Permission.objects.filter(content_type=assignment_perm)
        for p in perm:
            admin_assistant.permissions.add(p)

        note_perm = ContentType.objects.get(app_label='notes', model='note')
        perm = Permission.objects.filter(content_type=note_perm)
        for p in perm:
            admin_assistant.permissions.add(p)

        # school app
        section_perm = ContentType.objects.get(app_label='school', model='section')
        perms = Permission.objects.filter(content_type=section_perm)
        for p in perms:
            admin_assistant.permissions.add(p)

        grade_perm = ContentType.objects.get(app_label='school', model='grade')
        perms = Permission.objects.filter(content_type=grade_perm)
        for p in perms:
            admin_assistant.permissions.add(p)

        examtype_perm = ContentType.objects.get(app_label='school', model='examtype')
        perms = Permission.objects.filter(content_type=examtype_perm)
        for p in perms:
            admin_assistant.permissions.add(p)

        # users app
        student_profile = ContentType.objects.get(app_label='users', model='studentprofile')
        perms = Permission.objects.filter(content_type=student_profile)
        for p in perms:
            admin_assistant.permissions.add(p)

        teacher_profile = ContentType.objects.get(app_label='users', model='teacherprofile')
        perms = Permission.objects.filter(content_type=teacher_profile)
        for p in perms:
            admin_assistant.permissions.add(p)

        parent_profile = ContentType.objects.get(app_label='users', model='parentprofile')
        perms = Permission.objects.filter(content_type=parent_profile)
        for p in perms:
            admin_assistant.permissions.add(p)

        self.stdout.write('Successfully created Admin Assistant role')