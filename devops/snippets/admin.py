from django.contrib import admin

from .models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    """
    This is Django Admin for Snippets
    """
    list_display = ('id', 'title', 'owner')

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.user.is_staff
