# Generated by Django 5.1.4 on 2024-12-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSystem', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iterm',
            name='iterm',
        ),
        migrations.AddField(
            model_name='iterm',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='pictures/'),
        ),
    ]
