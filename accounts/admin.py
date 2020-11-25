from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
        
from .models import User

from .forms import *



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('phone', 'first_name', 'is_staff')
    list_filter = (['phone'])
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info', {'fields': ('avatar','first_name','last_name', 'dob')}),
        ('Permissions', {'fields': ('is_staff', 'is_active' )}),
        ('groups',{'fields': (['groups'])}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'),
        }),
    )
    search_fields = ( 'phone', 'first_name' )
    ordering = ( 'phone', 'first_name' )
    filter_horizontal = ()


    def get_inline_instance(self, request, obj=None):
    	if not obj:
    		return list()
    	return super(UserAdmin,self).get_inline_instance(request,obj)




# Now register the new UserAdmin...
admin.site.register(User,UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
#admin.site.unregister(Group)