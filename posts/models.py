from django.db import models
from django.utils import timezone

from users.models import User

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISH = "PB", "Published"
        REJECTED = "RJ", "Rejected"

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    publish = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publish"]
        indexes = [
            models.Index(fields=["-publish"])
        ]

    def __str__(self):
        return self.title