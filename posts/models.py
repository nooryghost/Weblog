from django.db import models

from users.models import User

STATUS = (
    ("Published", 1),
    ("Draft", 2)
)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS, default=2)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_time")
