# Generated by Django 3.0.3 on 2020-03-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0008_auto_20200324_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='photo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
