# Generated by Django 4.0.4 on 2022-05-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_rename_size_page_size_s'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(null=True, unique=True),
        ),
    ]
