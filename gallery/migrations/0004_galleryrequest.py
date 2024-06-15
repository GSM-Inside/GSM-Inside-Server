# Generated by Django 5.0.6 on 2024-06-15 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_gallery_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
