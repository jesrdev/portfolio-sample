# Generated by Django 3.2 on 2021-07-06 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image_name',
        ),
    ]