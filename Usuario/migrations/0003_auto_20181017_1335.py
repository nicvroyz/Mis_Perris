# Generated by Django 2.1.2 on 2018-10-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_auto_20181017_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.SlugField(max_length=10),
        ),
    ]