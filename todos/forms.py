from django import forms
from . import models


class CreateTodo(forms.ModelForm):
    class Meta:
        model = models.Todos
        fields = ['text', 'time']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Input your note here...'}),
            'time': forms.TimeInput(attrs={'placeholder': '00:00'})
        }
