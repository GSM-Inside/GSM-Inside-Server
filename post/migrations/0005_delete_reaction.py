# Generated by Django 5.0.3 on 2024-06-14 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_image_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reaction',
        ),
    ]
