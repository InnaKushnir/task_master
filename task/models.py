from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):

    class Meta:
        ordering = ["state_task", "create_datetime"]

    content = models.CharField(max_length=255)
    create_datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    state_task = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return f"{self.content} {self.tags} {self.state_task}"



