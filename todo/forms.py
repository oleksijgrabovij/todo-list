from todo.models import Task, Tag
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "content": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter task name..."}),
            "deadline": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "tags": forms.CheckboxSelectMultiple(),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control",
                       "placeholder": "Enter tag name..."
                }
            )
        }
