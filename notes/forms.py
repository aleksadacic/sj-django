from django import forms
from . import models


class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Notes
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Input your note here...'})
        }


class UpdateNote(forms.ModelForm):
    class Meta:
        model = models.Notes
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'editor init-values'})
        }
