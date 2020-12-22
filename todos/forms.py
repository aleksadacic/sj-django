from django import forms
from . import models


class CreateTodo(forms.ModelForm):
    class Meta:
        model = models.Todos
        fields = ['text', 'time']
