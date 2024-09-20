from django.contrib import admin
from .models import Post

# Menambahkan Post ke admin panel
admin.site.register(Post)
