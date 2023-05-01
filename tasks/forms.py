from django import forms
from .models import Task


class TaskCreationForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title']
        widgets = {'title':forms.TextInput(attrs={'class': 'w-full outline-none border-2 border-slate-300 p-3'}),}