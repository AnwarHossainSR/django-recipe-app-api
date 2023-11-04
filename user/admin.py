from django.contrib import admin
from .models import UserAccount
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserModelAdmin(BaseUserAdmin):
  # The fields to be used in displaying the User model.
  # These override the definitions on the base UserModelAdmin
  # that reference specific fields on auth.User.
  list_display = ('id', 'email', 'name', 'is_superuser')
  list_filter = ('is_superuser',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password',)}),
      ('Personal info', {'fields': ('name',)}),
      ('Permissions', {'fields': ('is_superuser',)}),
  )
  # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
  # overrides get_fieldsets to use this attribute when creating a user.
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'name',),
      }),
  )
  search_fields = ('email',)
  ordering = ('email', 'id')
  filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(UserAccount, UserModelAdmin)