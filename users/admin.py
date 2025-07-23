from django.contrib import admin
from .models import User
from django.utils import timezone

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_approved', 'is_active', 'is_staff')
    list_filter = ('role', 'is_approved', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    actions = ['approve_users']

    def approve_users(self, request, queryset):
        queryset.update(is_approved=True)
    approve_users.short_description = "Approve selected users"

    def save_model(self, request, obj, form, change):
        if 'is_approved' in form.changed_data and obj.is_approved and not obj.approved_at:
            obj.approved_at = timezone.now()
        super().save_model(request, obj, form, change)
