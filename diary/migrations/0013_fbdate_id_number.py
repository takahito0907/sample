# Generated by Django 3.0.3 on 2020-03-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0012_auto_20200324_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='fbdate',
            name='id_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='id'),
        ),
    ]
