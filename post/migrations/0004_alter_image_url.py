# Generated by Django 5.0.3 on 2024-06-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_image_image_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(),
        ),
    ]
