from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.form import TagForm, TaskForm
from task.models import Task, Tag


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task

    def get_context_data(self, *args, **kwargs):

        context = super(TaskListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task:tag-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.DeleteView):
    model = Task


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("task:tag-list")
