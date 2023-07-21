from django.contrib import admin

from tasks.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]
    list_filter = ["tag"]
    search_fields = ["tag"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "created_at", "deadline", "is_done"]
    list_filter = ["created_at"]
    search_fields = ["created_at"]
