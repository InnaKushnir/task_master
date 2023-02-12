from django import forms

from todo.models import Task, Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
