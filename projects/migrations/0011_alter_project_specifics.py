# Generated by Django 3.2 on 2021-07-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='specifics',
            field=models.TextField(),
        ),
    ]
