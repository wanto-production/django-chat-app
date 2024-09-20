from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)  # Judul Post
    content = models.TextField(unique=True)  # Konten Post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key ke user
    created_at = models.DateTimeField(auto_now_add=True)  # Tanggal dibuat
    updated_at = models.DateTimeField(auto_now=True)  # Tanggal update

    def __str__(self):
        return self.title