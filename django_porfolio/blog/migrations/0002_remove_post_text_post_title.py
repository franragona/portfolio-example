# Generated by Django 4.2.1 on 2023-05-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
