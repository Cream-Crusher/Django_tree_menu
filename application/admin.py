from django.contrib import admin
from application.models import TreeNode


class ChildInline(admin.TabularInline):
    model = TreeNode
    extra = 1


@admin.register(TreeNode)
class TreeNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_name', 'parent')
    list_filter = ('parent',)
    search_fields = ('display_name',)
    inlines = [ChildInline]
