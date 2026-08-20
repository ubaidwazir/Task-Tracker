from django import forms
from django.contrib.auth.models import User
from .models import Task, TaskAssignment

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["owner", "title", "description", "due_date", "completed_at", "status"]
        widgets = {
            "due_date": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "completed_at": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
        }


class AssignedToForm(forms.ModelForm):
    class Meta:
        model = TaskAssignment
        fields = ["user", "task"]
