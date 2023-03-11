from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "status", "created_time")
    list_filter = ("status",)
    search_fields = ["title", "author", "description"]
