from django.shortcuts import render, get_object_or_404
from .models import TreeNode


def show_page(request, pk=None):
    path_to_root = []

    if pk:
        target_node = get_object_or_404(TreeNode, id=pk)
    else:
        target_node = TreeNode.objects.get(parent__isnull=True)

    current_node = target_node
    path_to_root.append(load_node(current_node))

    while current_node.parent:
        path_to_root.append(load_node(current_node.parent))
        current_node = current_node.parent

    return render(request, 'index.html', context={'nodes': path_to_root})


def load_node(node):

    return {
        'node_id': node.id,
        'display_name': node.display_name,

        'parent': node.parent,
        'children': [child for child in node.children.all()]
    }
