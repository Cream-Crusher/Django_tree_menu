# Generated by Django 4.2.4 on 2023-10-06 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_rename_display_home_node_display_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(db_index=True, max_length=50)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='application.treenode')),
            ],
        ),
        migrations.DeleteModel(
            name='Node',
        ),
    ]
