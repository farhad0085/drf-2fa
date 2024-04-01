from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.utils.translation import ugettext_lazy as _


class UserAccountAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'full_name', 'is_staff', 'is_active')
    filter_horizontal = ['groups', 'user_permissions']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['email', 'first_name', 'last_name', 'id']
    ordering = ['email',]

    def full_name(self, obj):
        return obj.get_full_name()


admin.site.register(UserAccount, UserAccountAdmin)
