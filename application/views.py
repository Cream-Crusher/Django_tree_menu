from django.shortcuts import render, get_object_or_404
from .models import TreeNode


def show_page(request, pk=None):
    nodes_list = []

    if pk:
        node = get_object_or_404(TreeNode, id=pk)
        nodes_list.append(get_tree_json(node))
    else:
        nodes = TreeNode.objects.filter(parent__isnull=True)
        nodes_list = [get_tree_json(node) for node in nodes]

    return render(request, 'index.html', context={'nodes': nodes_list})


def get_tree_json(node):
    children = [get_tree_json(child) for child in node.children.all()]

    return {
        'node_id': node.id,
        'display_name': node.display_name,
        'children': children
    }
