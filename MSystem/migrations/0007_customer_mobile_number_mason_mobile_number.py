# Generated by Django 5.1.4 on 2024-12-21 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSystem', '0006_remove_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(default='000-000-0000', max_length=10),
        ),
        migrations.AddField(
            model_name='mason',
            name='mobile_number',
            field=models.CharField(default='000-000-0000', max_length=10),
        ),
    ]
