from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at', 'is_read')
    list_filter = ('subject', 'is_read', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('submitted_at',)
