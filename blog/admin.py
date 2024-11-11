from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "description", "image", "created_at", "view_count",)
    search_fields = ("title", "description",)
    list_filter = ("created_at", "view_count",)
