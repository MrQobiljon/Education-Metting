# Generated by Django 4.1.6 on 2023-04-16 09:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetting', '0003_navbar_created_at_alter_navbar_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuniversity',
            name='video',
            field=models.URLField(blank=True, help_text='Paste the youtube html code of the video', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.ImageField(help_text='Image size should be 270x170', upload_to='course/'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='photo',
            field=models.ImageField(help_text='Image size should be 370x215.', upload_to='meeting/'),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='video',
            field=models.FileField(help_text='Upload video.\nVideo resolution should be 960x600.', upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
        migrations.AlterField(
            model_name='strongest',
            name='logo',
            field=models.ImageField(help_text='Let the size of the logo be 60x60.', upload_to='strongest/'),
        ),
    ]
