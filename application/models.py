from django.db import models


class TreeNodeQuerySet(models.QuerySet):
    def loading_parent_queries(self):

        return self.select_related('parent')

    def loading_children_queries(self):

        return self.prefetch_related('children')


class TreeNode(models.Model):
    display_name = models.CharField(
        max_length=50,
        db_index=True
    )

    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    objects = TreeNodeQuerySet.as_manager()

    def __str__(self):
        return self.display_name
