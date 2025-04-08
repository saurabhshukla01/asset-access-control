from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Organization, Asset, User


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'secret_key', 'organization')
    list_filter = ('organization',)
    search_fields = ('name',)


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'organization', 'is_staff', 'is_active')
    list_filter = ('role', 'organization', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Organization Info', {'fields': ('organization', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'organization', 'role', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


# Unregister default Group if not used
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
