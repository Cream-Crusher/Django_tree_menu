from django.contrib import admin
from application.models import TreeNode


@admin.register(TreeNode)
class UserAdmin(admin.ModelAdmin):
    pass
