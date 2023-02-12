from django.contrib import admin

from todo.models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)
