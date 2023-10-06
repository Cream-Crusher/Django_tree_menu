from django.db import models


class Node(models.Model):
    display_name = models.CharField(
        max_length=50,
        db_index=True,
        null=False)

    parent = models.OneToOneField(
        'self',
        null=True,
        on_delete=models.CASCADE,
        related_name='child'
    )

    children = models.ManyToManyField(
        'self',
        blank=True,
        related_name='parents'
    )

    def __str__(self):
        return self.display_name
