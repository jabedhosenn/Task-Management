from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        
        widgets = {
            'description' : forms.Textarea(attrs={'rows':4}),
            'categories' : forms.CheckboxSelectMultiple 
        }
        