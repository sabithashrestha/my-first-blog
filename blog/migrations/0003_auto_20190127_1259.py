# Generated by Django 2.1.5 on 2019-01-27 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_writing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writing',
            name='author',
        ),
        migrations.DeleteModel(
            name='Writing',
        ),
    ]
