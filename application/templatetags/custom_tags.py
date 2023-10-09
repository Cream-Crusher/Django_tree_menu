from django import template
from django.urls import reverse
from django.http import Http404
from django.utils.safestring import mark_safe

from application.models import TreeNode


register = template.Library()


@register.simple_tag
def draw_menu(node_id):

    if node_id:  # Чистый SQL запрос для оптимизации древидного меню
        query_target_node = f'''
                WITH RECURSIVE tree AS (
          SELECT *
          FROM application_treenode WHERE id = { node_id }
          UNION ALL
            SELECT node.*
          FROM application_treenode AS node, tree AS t WHERE node.id = t.parent_id
        )
        SELECT * FROM tree
        JOIN application_treenode AS child ON tree.id = child.parent_id
        '''
    else:  # Чистый SQL запрос для оптимизации древидного меню
        query_target_node = '''
        SELECT * FROM application_treenode WHERE parent_id IS NULL;
        '''

    path_to_root = TreeNode.objects.raw(query_target_node, [node_id])

    if not path_to_root:
        raise Http404("Object not found")

    output_html_segment = draw_node(path_to_root[-1], path_to_root)

    return mark_safe(output_html_segment)


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
