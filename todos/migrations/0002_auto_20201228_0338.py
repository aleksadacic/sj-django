# Generated by Django 3.1.4 on 2020-12-28 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='text',
            field=models.TextField(max_length=30),
        ),
    ]
