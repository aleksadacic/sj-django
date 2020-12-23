from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    text = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.text[:5]

    def snippet(self):
        if len(self.text) >= 20:
            return self.text[:20] + "..."
        return self.text
