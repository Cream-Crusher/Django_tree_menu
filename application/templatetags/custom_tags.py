from django import template
from django.shortcuts import get_object_or_404

from application.models import TreeNode


register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    path_to_root = []

    if menu_name:
        target_node = get_object_or_404(TreeNode, id=menu_name)
    else:
        target_node = TreeNode.objects.get(parent__isnull=True)

    current_node = target_node
    path_to_root.append(load_node(current_node))

    while current_node.parent:
        path_to_root.append(load_node(current_node.parent))
        current_node = current_node.parent

    return path_to_root


def load_node(node):

    return {
        'node_id': node.id,
        'display_name': node.display_name,

        'parent': node.parent,
        'children': [child for child in node.children.all()]
    }
