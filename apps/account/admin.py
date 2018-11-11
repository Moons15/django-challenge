from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.site_header = 'Products Admministration'
admin.site.site_title = 'Challenge Admin'
admin.site.index_title = 'Challenge Admin'

class User_Admin(UserAdmin):
    fieldsets = (
        (None, {'fields': (
            'email', 'password', 'cellphone', 'country', 'is_superuser')}),
        (('Personal info'),
         {'fields': ('first_name', 'last_name', 'email',)}),
        (('Important dates'),
         {'fields': ('request_date', 'last_login', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['id', 'email', 'first_name', 'last_name', 'is_active',
                    'created_at']
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name', 'email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, User_Admin)
