from django import forms
from .models import Chapter
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['name', 'letters', 'rush_chair', 'president', 'info', 'chapter_size']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields must be a dictionary structure, so can't do f.widget, f.label, etc
        for f in self.fields:
            # set each field's placeholder text to its name
            self.fields[f].widget.attrs.update({'placeholder': self.fields[f].label})