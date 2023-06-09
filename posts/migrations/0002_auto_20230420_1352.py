# Generated by Django 3.2.18 on 2023-04-20 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='camera_type',
            field=models.CharField(choices=[('dslr_camera', 'DSLR Camera'), ('mirrorless_camera', 'Mirrorless Camera'), ('bridge_camera', 'Bridge Camera'), ('compact_digital_camera', 'Compact Digital Camera'), ('smartphone', 'Smartphone')], default='other', max_length=32),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_type',
            field=models.CharField(choices=[('abstract', 'Abstract'), ('action', 'Action'), ('animals', 'Animals'), ('architecture', 'Architecture'), ('black_and_white', 'Black and White'), ('colors', 'Colors'), ('city', 'City'), ('fashion', 'Fashion'), ('food', 'Food'), ('landscape', 'Landscape'), ('macro', 'Macro'), ('manipulation', 'Manipulation'), ('nature', 'Nature'), ('night', 'Night'), ('objects', 'Objects'), ('people', 'People'), ('transportation', 'Transportation'), ('water', 'Water'), ('wedding', 'Wedding')], default='other', max_length=32),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_yyxugh', upload_to='images/'),
        ),
    ]
