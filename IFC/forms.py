from django import forms
from .models import Chapter
from django.contrib.auth.models import User

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['name', 'letters', 'rush_chair', 'president', 'info', 'chapter_size']

class RegisterForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_conf']

    def save(self, commit=True):
        user = super()

    password = forms.CharField