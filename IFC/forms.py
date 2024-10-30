from django import forms
from .models import Chapter
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['letters', 'rush_chair', 'president', 'info', 'chapter_size', 'image']


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
