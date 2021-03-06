# Generated by Django 2.1.2 on 2018-10-19 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0007_auto_20181019_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=1234, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='password_verification',
            field=models.CharField(default=1234, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.SlugField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
