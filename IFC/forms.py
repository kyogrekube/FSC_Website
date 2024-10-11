from django import forms
from .models import Chapter
    
class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['name', 'letters', 'rush_chair', 'president', 'info', 'chapter_size']  # Select the fields you want to allow users to edit