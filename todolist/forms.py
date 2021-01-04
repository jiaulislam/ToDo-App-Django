from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # "type": "text",
                "class": "form-control form-control-lg rounded-0",
                "placeholder": "Enter task...",
            }
        ),
    )

    completed = forms.CharField(
        required = False,
        widget= forms.widgets.CheckboxInput(
            attrs={
                "type": "checkbox",
                "class": "from-check-input",
            }
        ),
    )