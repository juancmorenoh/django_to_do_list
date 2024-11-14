from django.db import models

#define model representing each task
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # define the string representation of the Task object
    def __str__(self):
        return self.title