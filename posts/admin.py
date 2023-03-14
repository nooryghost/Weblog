from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "status", "publish"]
    list_filter = ["status", "publish", "author"]
    search_fields = ["title", "author", "slug", "description"]
    ordering = ["publish"]
    raw_id_fields = ["author"]
    prepopulated_fields = {"slug": ["title"]}
    list_editable = ["status"]