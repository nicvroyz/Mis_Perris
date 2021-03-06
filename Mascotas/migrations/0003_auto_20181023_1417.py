# Generated by Django 2.1.2 on 2018-10-23 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0008_auto_20181019_2025'),
        ('Mascotas', '0002_auto_20181020_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='usuario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mascota',
            name='fotografia',
            field=models.ImageField(default='img_folder/None/no-img.jpg', upload_to=''),
        ),
    ]
