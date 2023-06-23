from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    deadLine = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return f'{self.title}'