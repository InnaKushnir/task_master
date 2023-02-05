from django.contrib import admin

from task.models import Task, Tag

admin.site.register(Task)
admin.site.register(Tag)
