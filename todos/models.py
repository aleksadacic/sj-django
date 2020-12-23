from django.db import models
from django.contrib.auth.models import User


class Todos(models.Model):
    text = models.TextField(max_length=30)
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.text[:5]

