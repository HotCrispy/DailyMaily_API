from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Model_User as User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_superuser', 'date_joined')
    list_display_links = ('username',)
    list_filter = ('is_superuser', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username', )}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    search_fields = ('email','username')
    ordering = ('-date_joined',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
