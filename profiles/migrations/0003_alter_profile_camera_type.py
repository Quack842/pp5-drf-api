# Generated by Django 3.2.18 on 2023-05-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_camera_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='camera_type',
            field=models.CharField(choices=[('dslr_camera', 'DSLR Camera'), ('mirrorless_camera', 'Mirrorless Camera'), ('bridge_camera', 'Bridge Camera'), ('compact_digital_camera', 'Compact Digital Camera'), ('smartphone', 'Smartphone')], default='All', max_length=100),
        ),
    ]