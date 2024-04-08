# Generated by Django 5.0.3 on 2024-04-06 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_attachments_tasklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.tasklist'),
            preserve_default=False,
        ),
    ]