from django.db import models
from django.contrib.auth.models import User


class Todos(models.Model):
    text = models.TextField(max_length=240)
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    counter = 0

    def __str__(self):
        self.counter += 1
        return self.counter + "-todo"
