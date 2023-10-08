from django import template
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from application.models import TreeNode


register = template.Library()


@register.simple_tag
def draw_menu(node_id):
    path_to_root = []

    if node_id:
        target_node = get_object_or_404(TreeNode, id=node_id)
    else:
        target_node = TreeNode.objects.get(parent__isnull=True)

    current_node = target_node
    path_to_root.append(current_node)

    while current_node.parent:
        path_to_root.append(current_node.parent)
        current_node = current_node.parent

    draw_nodes = draw_node(path_to_root[-1], path_to_root)

    return mark_safe(draw_nodes)


def draw_node(node, path_to_root):

    output_str = ''

    href_str = reverse('show_page', args=[node.id])
    output_str += f"""<a href={href_str}>{node.display_name}: {node.id}</a><ul>"""

    for child in node.children.all():
        if child in path_to_root:
            output_str += f"""<li>{draw_node(child, path_to_root)}</li>"""
        else:
            href_str = reverse('show_page', args=[child.id])
            output_str += f"""<li><a href={href_str}>{child.display_name}: {child.id}</li></a>"""

    output_str += f"""</ul>"""

    return output_str
