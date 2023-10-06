from django.shortcuts import render, get_object_or_404
from .models import TreeNode


def show_page(request, pk=None):
    if pk:
        target_node = get_object_or_404(TreeNode, id=pk)
    else:
        target_node = TreeNode.objects.get(parent__isnull=True)

    return render(request, 'index.html', context={'target_node': load_node(target_node)})


def load_node(node):

    return {
        'node_id': node.id,
        'display_name': node.display_name,

        'parent': node.parent,
        'children': [child for child in node.children.all()]
    }
