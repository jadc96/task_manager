from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    # avatar = models.ImageField(null=True, default="avatar.svg")

class TaskCategory(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Task(models.Model):
    description = models.CharField(max_length=200)
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(blank=True)
    place = models.CharField(max_length=200, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
