from django.db import models

# Create your models here.

class Message(models.Model):
    """docstring for Messege."""
    text = models.TextField()

    def __str__(self):
        return self.text
