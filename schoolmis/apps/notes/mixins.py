from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse

from .models import Note, Assignment
from .forms import NoteForm, AssignmentForm


class NoteMixin(LoginRequiredMixin):
    model = Note
    form_class = NoteForm
    context_object_name = 'note'

    def get_success_url(self):
        return reverse('note_assignment:note_list')


class AssignmentMixin(LoginRequiredMixin):
    model = Assignment
    form_class = AssignmentForm
    context_object_name = 'assignment'

    def get_success_url(self):
        return reverse('note_assignment:assignment_list')