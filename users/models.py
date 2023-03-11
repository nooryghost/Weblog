from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    description = models.TextField()
    avatar = models.ImageField(upload_to="images/avatars/", default="images/profile.jpg")
