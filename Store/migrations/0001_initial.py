# Generated by Django 4.0.4 on 2022-05-06 18:58

import Store.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(default=Store.models.default_city, max_length=30)),
                ('state', models.CharField(max_length=2)),
                ('date', models.DateField(default=datetime.date(2022, 5, 6))),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255, unique=True)),
                ('price', models.IntegerField()),
                ('url', models.URLField(unique=True)),
                ('size', models.CharField(choices=[('U', 'Unknown'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'XLarge'), ('XXL', 'XXLarge')], default='U', max_length=3)),
                ('topic_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.topic')),
            ],
        ),
        migrations.CreateModel(
            name='DataAccessed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.page')),
            ],
        ),
    ]
