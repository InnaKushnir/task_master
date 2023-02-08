from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):

    content = models.CharField(max_length=255)
    create_datetime = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    state_task = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["state_task", "-create_datetime"]

    def __str__(self):
        return f"{self.content}  {self.create_datetime}  {self.tags}  {self.state_task}"
