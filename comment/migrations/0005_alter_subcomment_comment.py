# Generated by Django 5.0.6 on 2024-06-17 05:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_alter_subcomment_subcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcomment',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcomments', to='comment.comment'),
        ),
    ]