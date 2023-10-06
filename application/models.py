from django.db import models


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

    def __str__(self):
        return self.display_name
