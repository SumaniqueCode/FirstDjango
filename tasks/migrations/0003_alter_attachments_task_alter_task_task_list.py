# Generated by Django 5.0.3 on 2024-04-06 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_attachments_tasklist_task_task_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachments',
            name='task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='tasks.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.tasklist'),
        ),
    ]