from django import forms
from .models import Task


# Define a form for creating and updating Task instances
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']