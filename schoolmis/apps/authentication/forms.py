from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries import countries

from PIL import Image
from django import forms
from django.core.files import File

from dal import autocomplete

from apps.school.models import Grade
from apps.users.models import ParentProfile, StudentProfile, TeacherProfile

GENDER_TYPE = (('MALE', 'Male'),
               ('FEMALE', 'Female'),
               ('OTHER', 'Other')

               )

COUNTRY_CHOICES = tuple(countries)


class ProfileForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    file = forms.ImageField()

    def save(self):
        photo = super(ProfileForm, self).save()
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w + x, h + y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo

class StudentForm(ProfileForm):

    class Meta:
        model = StudentProfile
        fields = ('x', 'y', 'width', 'height', 'first_name', 'middle_name', 'last_name', 'email', 'phone', 'roll_no', 'section', 'temporary_address',
                  'permanent_address', 'blood_group', 'dob', 'file')

class ParentForm(ProfileForm):

    class Meta:
        model = ParentProfile
        fields = ('x', 'y', 'width', 'height', 'first_name', 'middle_name', 'last_name', 'email', 'phone', 'temporary_address', 'permanent_address',
              'blood_group', 'dob', 'occupation', 'file')


class TeacherForm(ProfileForm):

    class Meta:
        model = TeacherProfile
        fields = ('x', 'y', 'width', 'height', 'first_name', 'middle_name', 'last_name', 'email', 'phone', 'temporary_address', 'permanent_address',
              'blood_group', 'dob', 'education', 'file')


class UserProfileForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(required=False)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    phone = forms.CharField(max_length=250)
    temporary_address = forms.CharField(max_length=250)
    permanent_address = forms.CharField(max_length=250)
    nationality = forms.ChoiceField(choices=COUNTRY_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].help_text = None


class TeacherSignupForm(UserProfileForm):

    education = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'password1', 'password2', 'email', 'gender',
                  'phone', 'temporary_address', 'permanent_address', 'nationality', 'education']


class StudentSignupForm(UserProfileForm):

    grade = forms.ModelChoiceField(queryset=Grade.objects.all())
    parent = forms.ModelChoiceField(
            queryset=ParentProfile.objects.all(),
            widget=autocomplete.ModelSelect2(url='authentication:parent_autocomplete')
    )

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'password1', 'password2', 'email', 'gender',
                  'phone', 'temporary_address', 'permanent_address', 'nationality', 'grade', 'parent']


class ParentSignupForm(UserProfileForm):

    occupation = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'username', 'password1', 'password2', 'email', 'gender', 'phone',
                  'temporary_address', 'permanent_address', 'nationality', 'occupation']
